import sys, socket

from ServerWorker import ServerWorker

class Server:	
	
	def main(self):
		try:
			SERVER_PORT = int(sys.argv[1])
		except:
			print("[Usage: Server.py Server_port]\n")
		rtspSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # type SOCK_STREAM cho các giao thức hướng kêt nối
		rtspSocket.bind(('', SERVER_PORT)) # gắn kết địa chỉ (hostname, port number) tới Socket
		rtspSocket.listen(5) # chờ 5s kết nối Client   

		# Receive client info (address,port) through RTSP/TCP session
		while True:
			clientInfo = {}
			clientInfo['rtspSocket'] = rtspSocket.accept() # Thiet lap ket noi voi client.
			ServerWorker(clientInfo).run() # class ServerWorker gọi hàm run()

if __name__ == "__main__":
	(Server()).main()


