#!/usr/bin/env python3
import socket
import time

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as start:
        host = "www.google.com"
        port = 80

        #QUESTION 3
        start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #bind socket to address
        start.bind((HOST, PORT))
        #set to listening mode
        start.listen(2)
        while True:
            conn, addr = start.accept()
            print("Connected by", addr)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as end:
                remote_ip = get_remote_ip(host)
                end.connect((remote_ip , port))
                data = conn.recv(BUFFER_SIZE)
                end.sendall(data)
                end.shutdown(socket.SHUT_WR)

                final_data = end.recv(BUFFER_SIZE)
                conn.send(final_data)
            
            conn.close()
if __name__ == "__main__":
    main()


                