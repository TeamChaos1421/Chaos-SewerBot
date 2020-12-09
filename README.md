# Chaos-SewerBot
doing stuffs with raspberry pi to control the Storm Drain Bot

## Server:
**Work-in-Progress**
to be run on the RasPi, creates a socket server and prints clients info upon connection and data recieved

## Client:
Modified code from XInput-Python's `XInputTest.py` to send right stick X and Y Values to the RasPi Server over Socket

## Dependencies:
### Server:
1. Python3

### Client:
1. Windows Based PC (to use XInput)
2. Python3
3. XInput-Python (`Pip install Xinput-Python` to install)

## Installation & Setup:
1. Flash an up-to-date version of `Raspberry OS Lite` to a Micro-SD Card
2. Create a file named `ssh` (without a file extension) to enable ssh
3. Insert the Micro-SD, ethernet, and power into the Pi and Boot it up.
4. SSH Into the Pi and enter `Raspi-Config` to change the hostname to "Chaos" (Or via editing `/etc/hosts`)
5. Run `sudo apt-get update && sudo apt-get install samba` to install samba
6. Replace `/etc/samba/smb.conf` with the file in the Repo & Run `sudo systemctl enable smbd` along with `sudo systemctl start smbd`
7. On a Windows Host Machine, Run (`Win+R`) \\chaos
8. Place Both `Server.py` and `Client.py` in the `Home` folder

## Usage:
1. SSH into the Pi and run `python3 server.py` to start the server
2. Double Click `client.py` to start the client.
3. The server will print the cliend address and socket along with the [Y,X] Values of the Right Stick
