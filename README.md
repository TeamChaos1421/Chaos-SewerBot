# Chaos-SewerBot
doing stuffs with raspberry pi to control the Storm Drain Bot

## Server:
**Work-in-Progress**
to be run on the RasPi, creates a socket server and prints clients info upon connection and data recieved

## Client:
Modified code from XInput-Python's `XInputTest.py` to send right stick X and Y Values to the RasPi Server over Socket

## Dependencies:
### Server:
1. python3 python3-rpi.gpio

### Client:
1. Windows Based PC (to use XInput)
2. Python3
3. XInput-Python (`Pip install Xinput-Python` to install)

## Installation & Setup:
1. Flash an up-to-date version of `Raspberry OS Lite` to a Micro-SD Card (we used Buster)
2. Open the boot volume and create a file named `ssh` (without a file extension) to enable ssh
3. Insert the Micro-SD, ethernet, and power into the Pi and Boot it up.
4. SSH Into the Pi and enter `Raspi-Config` to change the hostname to 'Chaos' (without '')
5. Run `sudo apt-get update && sudo apt-get install samba python3-rpi.gpio motion` to install prerequisites (make sure to select YES when the samba installation asks to configure 'WINS'
6. Replace `/etc/samba/smb.conf` with `smb.conf` in the Repo & Run `sudo systemctl enable smbd && sudo reboot`
7. Replace `/etc/motion/motion.conf` with `motion.conf` in the Repo and Run `sudo systemctl enable motion && sudo reboot`
8. On a Windows Host Machine, Run (`Win+R`) `\\chaos` (username:password is pi:raspberry)
9. Place Both `Server.py` `Client.py`, and `start' in the `Home` folder
10. Run chmod +x start to make the script executable

## Hardware Setup:
1. user jumper cables to connect the 5V pin on one of the PWM cables to pin 2 of Pi, PWM ground to Pin 6, throttle PWM data to pin11 and turn PWM data to pin 12

## Usage:
1. SSH into the Pi and run `./start` to start the server
2. Run `client.py` on the control computer to start the client.
3. The server will accept incoming client connections and control the bot
4. navigate to chaos:8081 in a web browser to view the live video feed
