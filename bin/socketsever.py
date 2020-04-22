from socket import *
server_port = 5050
buffer_size = 1024

server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind(('',server_port))
server_socket.listen(2)

while True:

    c,ip = server_socket.accept()
    print(c,ip)
    try:
        data = c.recv(buffer_size)
        c.send("hello".encode("utf-8"))
    except Exception as e:
        print(e)
    else:   
        c.close()

# while True:
#     # Establish connection with client.    
#     c, (client_host, client_port) = server_socket.accept()
#     # print 'Got connection from', client_host, client_port
#     # s.recv(1000)
#     c.send(bytes('Server Online\n',"utf-8"))
#     c.send(bytes('HTTP/1.0 200 OK\n',"utf-8"))
#     c.send(bytes('Content-Type: text/html\n',"utf-8"))
#     # c.send(bytes(' """\n <p>hello</p> """ ',"utf-8"))
#     c.close()