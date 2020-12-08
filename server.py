#!/usr/bin/env python3

import socket
import json

# x = 0

HOST = ''                                               # Standard loopback interface address (localhost)
PORT = 4444                                                         # Port to listen on (non-privileged ports are > 1023)
data = [0, 0]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)         # Reuse Sockets to aovid having to restart the script
	s.bind((HOST, PORT))                                            # Bind Socket
	s.listen()                                                      # Begin listening
	while 1:
		try:
			conn, addr = s.accept()                                     # Accept Incoming connection
			with conn:
				print('Connected by', addr)
				while True:
					data = conn.recv(1024)
					if not data:
						break
					conn.sendall(b'OK')
					print('throttle:  ' + str(json.loads(data)[0]))
					print('turn:      ' + str(json.loads(data)[1]))
					# x = x + 1                                         # used to count connections
					# print(x)                                        
		except KeyboardInterrupt:
			exit()
			print("you're an idiot")
		except:
			print("your'e an idiot")