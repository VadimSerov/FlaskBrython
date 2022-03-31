import socket

if __name__ == '__main__':
	try:
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind(('127.0.0.1',4000))
		server.listen(4)

		i=0
		while True:
			#print('Working...')
			client_socket, addres = server.accept()
			data = client_socket.recv(1024).decode('utf-8')
			#print(data)
			HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html ; charset=utf-8\r\n\r\n'
			file = open('index.html')
			responce = file.read()
			s=HDRS+responce+str(i)
			#s=responce
			file.close()
			content = s.encode('utf-8')
			i+=1
			client_socket.send(content)
			client_socket.shutdown(socket.SHUT_WR)
	except KeyboardInterrupt:
		server.close()
		#print('shhhh ')
