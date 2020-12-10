from XInput import *
import socket
import json
from time import sleep

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
    
HOST = '192.168.1.84'																	# The server's hostname or IP address
PORT = 4444																				# The port used by the server

root = tk.Tk()
root.title("Chaos 1421")
canvas = tk.Canvas(root, width= 600, height = 400, bg="white")
canvas.pack()

set_deadzone(DEADZONE_TRIGGER,10)

class Controller:																		# setup XInput Preview
    def __init__(self, center):
        self.center = center

        self.on_indicator_pos = (self.center[0], self.center[1] - 50)

        self.on_indicator = canvas.create_oval(((self.on_indicator_pos[0] - 10, self.on_indicator_pos[1] - 10), (self.on_indicator_pos[0] + 10, self.on_indicator_pos[1] + 10)))
        
        self.r_thumb_pos = (self.center[0] + 50, self.center[1] + 20)

        r_thumb_outline = canvas.create_oval(((self.r_thumb_pos[0] - 25, self.r_thumb_pos[1] - 25), (self.r_thumb_pos[0] + 25, self.r_thumb_pos[1] + 25)))

        r_thumb_stick_pos = self.r_thumb_pos

        self.r_thumb_stick = canvas.create_oval(((r_thumb_stick_pos[0] - 10, r_thumb_stick_pos[1] - 10), (r_thumb_stick_pos[0] + 10, r_thumb_stick_pos[1] + 10)))

        self.l_thumb_pos = (self.center[0] - 100, self.center[1] - 20)

        l_thumb_outline = canvas.create_oval(((self.l_thumb_pos[0] - 25, self.l_thumb_pos[1] - 25), (self.l_thumb_pos[0] + 25, self.l_thumb_pos[1] + 25)))

        l_thumb_stick_pos = self.l_thumb_pos

        self.l_thumb_stick = canvas.create_oval(((l_thumb_stick_pos[0] - 10, l_thumb_stick_pos[1] - 10), (l_thumb_stick_pos[0] + 10, l_thumb_stick_pos[1] + 10)))

        self.l_trigger_pos = (self.center[0] - 120, self.center[1] - 70)

        l_trigger_outline = canvas.create_rectangle(((self.l_trigger_pos[0] - 5, self.l_trigger_pos[1] - 20), (self.l_trigger_pos[0] + 5, self.l_trigger_pos[1] + 20)))

        l_trigger_index_pos = (self.l_trigger_pos[0], self.l_trigger_pos[1] - 20)

        self.l_trigger_index = canvas.create_rectangle(((l_trigger_index_pos[0] - 10, l_trigger_index_pos[1] - 5), (l_trigger_index_pos[0] + 10, l_trigger_index_pos[1] + 5)))

        self.r_trigger_pos = (self.center[0] + 120, self.center[1] - 70)

        r_trigger_outline = canvas.create_rectangle(((self.r_trigger_pos[0] - 5, self.r_trigger_pos[1] - 20), (self.r_trigger_pos[0] + 5, self.r_trigger_pos[1] + 20)))

        r_trigger_index_pos = (self.r_trigger_pos[0], self.r_trigger_pos[1] - 20)

        self.r_trigger_index = canvas.create_rectangle(((r_trigger_index_pos[0] - 10, r_trigger_index_pos[1] - 5), (r_trigger_index_pos[0] + 10, r_trigger_index_pos[1] + 5)))

        buttons_pos = (self.center[0] + 100, self.center[1] - 20)

        A_button_pos = (buttons_pos[0], buttons_pos[1] + 20)

        B_button_pos = (buttons_pos[0] + 20, buttons_pos[1])

        Y_button_pos = (buttons_pos[0], buttons_pos[1] - 20)

        X_button_pos = (buttons_pos[0] - 20, buttons_pos[1])

        self.A_button = canvas.create_oval(((A_button_pos[0] - 10, A_button_pos[1] - 10), (A_button_pos[0] + 10, A_button_pos[1] + 10)))

        self.B_button = canvas.create_oval(((B_button_pos[0] - 10, B_button_pos[1] - 10), (B_button_pos[0] + 10, B_button_pos[1] + 10)))

        self.Y_button = canvas.create_oval(((Y_button_pos[0] - 10, Y_button_pos[1] - 10), (Y_button_pos[0] + 10, Y_button_pos[1] + 10)))

        self.X_button = canvas.create_oval(((X_button_pos[0] - 10, X_button_pos[1] - 10), (X_button_pos[0] + 10, X_button_pos[1] + 10)))

        dpad_pos = (self.center[0] - 50, self.center[1] + 20)

        self.dpad_left = canvas.create_rectangle(((dpad_pos[0] - 30, dpad_pos[1] - 10), (dpad_pos[0] - 10, dpad_pos[1] + 10)), outline = "")

        self.dpad_up = canvas.create_rectangle(((dpad_pos[0] - 10, dpad_pos[1] - 30), (dpad_pos[0] + 10, dpad_pos[1] - 10)), outline = "")

        self.dpad_right = canvas.create_rectangle(((dpad_pos[0] + 10, dpad_pos[1] - 10), (dpad_pos[0] + 30, dpad_pos[1] + 10)), outline = "")

        self.dpad_down = canvas.create_rectangle(((dpad_pos[0] - 10, dpad_pos[1] + 10), (dpad_pos[0] + 10, dpad_pos[1] + 30)), outline = "")

        dpad_outline = canvas.create_polygon(((dpad_pos[0] - 30, dpad_pos[1] - 10), (dpad_pos[0] - 10, dpad_pos[1] - 10), (dpad_pos[0] - 10, dpad_pos[1] - 30), (dpad_pos[0] + 10, dpad_pos[1] - 30),
                                              (dpad_pos[0] + 10, dpad_pos[1] - 10), (dpad_pos[0] + 30, dpad_pos[1] - 10), (dpad_pos[0] + 30, dpad_pos[1] + 10), (dpad_pos[0] + 10, dpad_pos[1] + 10),
                                              (dpad_pos[0] + 10, dpad_pos[1] + 30), (dpad_pos[0] - 10, dpad_pos[1] + 30), (dpad_pos[0] - 10, dpad_pos[1] + 10), (dpad_pos[0] - 30, dpad_pos[1] + 10)),
                                             fill = "", outline = "black")

        back_button_pos = (self.center[0] - 20, self.center[1] - 20)

        self.back_button = canvas.create_oval(((back_button_pos[0] - 5, back_button_pos[1] - 5), (back_button_pos[0] + 5, back_button_pos[1] + 5)))

        start_button_pos = (self.center[0] + 20, self.center[1] - 20)

        self.start_button = canvas.create_oval(((start_button_pos[0] - 5, start_button_pos[1] - 5), (start_button_pos[0] + 5, start_button_pos[1] + 5)))

        l_shoulder_pos = (self.center[0] - 90, self.center[1] - 70)

        self.l_shoulder = canvas.create_rectangle(((l_shoulder_pos[0] - 20, l_shoulder_pos[1] - 5), (l_shoulder_pos[0] + 20, l_shoulder_pos[1] + 10)))

        r_shoulder_pos = (self.center[0] + 90, self.center[1] - 70)

        self.r_shoulder = canvas.create_rectangle(((r_shoulder_pos[0] - 20, r_shoulder_pos[1] - 10), (r_shoulder_pos[0] + 20, r_shoulder_pos[1] + 5)))

controllers = (Controller((150., 100.)),
               Controller((450., 100.)),
               Controller((150., 300.)),
               Controller((450., 300.)))


while 1:
	try: 																				# If it breaks, Try Again
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			# data = [input(), input()]
			t = 1
			while t:																	# Loop retry server connect until success
				try:
					s.connect((HOST, PORT))                         	    		    # Connect to RPi
					t = 0
				except:
					print("Failed to connect to server, Retrying in 5 Seconds.")
					sleep(4)
					print("Retrying...")
					sleep(1)
			while 1:
				events = get_events()
				for event in events:
					controller = controllers[event.user_index]
					if event.type == EVENT_CONNECTED:
						canvas.itemconfig(controller.on_indicator, fill="light green")
						
					elif event.type == EVENT_DISCONNECTED:
						canvas.itemconfig(controller.on_indicator, fill="")
						
					elif event.type == EVENT_STICK_MOVED:
						if event.stick == LEFT:
							l_thumb_stick_pos = (int(round(controller.l_thumb_pos[0] + 25 * event.x,0)), int(round(controller.l_thumb_pos[1] - 25 * event.y,0)))
							canvas.coords(controller.l_thumb_stick, (l_thumb_stick_pos[0] - 10, l_thumb_stick_pos[1] - 10, l_thumb_stick_pos[0] + 10, l_thumb_stick_pos[1] + 10))
							
						elif event.stick == RIGHT:
							data = [int(round(event.y * 127)), int(round(event.x * 127))]
							print(data)													#prints what the server should be receiving
							s.sendall(str.encode(json.dumps(data), 'utf-8'))            # okay, so this line dumps 'data' as a json string, encodes in in UTF-8, and sends in the the RPi in one command
																						
							data = s.recv(1024)                                         # Recieves the response from RPi "Should be 'OK'"    
							print('Received:', data.decode())                           # Outputs RPi's response to console                            
							sleep(0.001)												# Slows Code to save on CPU and Network Resources
							r_thumb_stick_pos = (int(round(controller.r_thumb_pos[0] + 25 * event.x,0)), int(round(controller.r_thumb_pos[1] - 25 * event.y,0)))
							canvas.coords(controller.r_thumb_stick, (r_thumb_stick_pos[0] - 10, r_thumb_stick_pos[1] - 10, r_thumb_stick_pos[0] + 10, r_thumb_stick_pos[1] + 10))

				try:          
					root.update()
				except tk.TclError:
					break
	except ConnectionAbortedError:														# Loops back to retry connection upon connection loss
		print("Lost Connection to Server, Retrying in 5 Seconds.")
		sleep(5)