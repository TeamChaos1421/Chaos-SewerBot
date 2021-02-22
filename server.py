#!/usr/bin/env python3

import socket
import json
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)                                            # prepare GPIO for PWM on ports 11 and 12
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
servo1 = GPIO.PWM(11,50)
servo2 = GPIO.PWM(12,50)

servo1.start(0)                                                     # Initialize PWM Outputs
servo2.start(0)

# x = 0

HOST = ''                                             				# Standard loopback interface address (localhost)
PORT = 4444                                                         # Port to listen on (non-privileged ports are > 1023)
data = [0, 0]
print("Server Started")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)         # Reuse Sockets to aovid having to restart the script
	s.bind((HOST, PORT))                                            # Bind Socket
	s.listen()                                                      # Begin listening
	while 1:
		try:
			conn, addr = s.accept()                                	# Accept Incoming connection
			with conn:
				print('Connected by', addr)
				while True:
					data = conn.recv(1024)
					if not data:
						break
					conn.sendall(b'OK')
					print('throttle:  ' + str(json.loads(data)[0]))
					print('turn:      ' + str(json.loads(data)[1]))
					servo1.ChangeDutyCycle((json.loads(data)[0] / 40) + 6)
					servo2.ChangeDutyCycle((json.loads(data)[1] / 40) + 6)
		except KeyboardInterrupt:
			exit()
			GPIO.cleanup()
		except:
			print("your'e an idiot")