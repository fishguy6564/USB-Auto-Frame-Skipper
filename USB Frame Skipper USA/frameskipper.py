import time
import struct
import usb.core
import usb.util
from Date import *

global_dev = None
global_out = None
global_in = None

#Sends string commands to the switch
def sendCommand(content):
    global_out.write(struct.pack("<I", (len(content)+2)))
    global_out.write(content)

#Using method from Goldleaf
def connect_switch():
    global global_dev
    global global_out
    global global_in
    global_dev = usb.core.find(idVendor=0x057E, idProduct=0x3000)
    if global_dev is not None:
        try:
            global_dev.set_configuration()
            intf = global_dev.get_active_configuration()[(0,0)]
            global_out = usb.util.find_descriptor(intf,custom_match=lambda e:usb.util.endpoint_direction(e.bEndpointAddress)==usb.util.ENDPOINT_OUT)
            global_in = usb.util.find_descriptor(intf,custom_match=lambda e:usb.util.endpoint_direction(e.bEndpointAddress)==usb.util.ENDPOINT_IN)
            return True
        except:
            return False
            pass
    else:
        return False

#To communicate with the user
def attemptConnection():
	isConnected = False
	while not isConnected:
		if connect_switch():
			print("Connected to Switch Successfully!")
			isConnected = True
		else:
			print("Failed to Connect to Switch!")
			print("Attempting to Reconnect in 5 Seconds...")
			time.sleep(5)

def increaseDay():
	sendCommand("press DLEFT")
	time.sleep(0.55)
	sendCommand("release DLEFT")
	time.sleep(0.1)
	sendCommand("click DUP")
	time.sleep(0.1)

	sendCommand("press DRIGHT")
	time.sleep(0.55)
	sendCommand("release DRIGHT")
	time.sleep(0.1)
	sendCommand("click A")

def increaseMonth():
	sendCommand("press DLEFT")
	time.sleep(0.55)
	sendCommand("release DLEFT")
	time.sleep(0.1)
	sendCommand("click DUP")
	time.sleep(0.1)
	sendCommand("click DLEFT")
	time.sleep(0.1)
	sendCommand("click DUP")
	time.sleep(0.1)
	sendCommand("press DRIGHT")
	time.sleep(0.6)
	sendCommand("release DRIGHT")
	time.sleep(0.1)
	sendCommand("click A")

def increaseYear():
	sendCommand("press DLEFT")
	time.sleep(0.5)
	sendCommand("release DLEFT")
	time.sleep(0.1)
	sendCommand("click DUP")
	time.sleep(0.1)
	sendCommand("click DLEFT")
	time.sleep(0.1)
	sendCommand("click DUP")
	time.sleep(0.1)
	sendCommand("click DLEFT")
	time.sleep(0.1)
	sendCommand("click DUP")
	time.sleep(0.1)
	sendCommand("press DRIGHT")
	time.sleep(0.6)
	sendCommand("release DRIGHT")
	time.sleep(0.1)
	sendCommand("click A")

#This version is developed for the USA date format. I will implement other date formats at a later date.
def main():
	attemptConnection()

	while True:
		try:
			frameAmt = int(input("Please enter the amount of frames you wish to skip: "))
			break
		except ValueError:
			print("Please input your frames as a whole number!")

	while True:
		try:
			month, day, year = input("Please enter the current date (on your switch) in the format MM/DD/YYYY:\n").split("/")
			currentDate = Date(int(month), int(day), int(year))
			break
		except:
			print("Please input your date in the format MM/DD/YYYY!")
	print("Performing date skipping...")
	
	for i in range(frameAmt - 1):
		sendCommand("click A")
		time.sleep(0.2)

		if not currentDate.increaseDay():
			if not currentDate.increaseMonth():
				currentDate.increaseYear()
				increaseYear()
			else:
				increaseMonth()
		else:
			increaseDay()
		time.sleep(0.2)
	print("Date skipping complete!")
	

	

main()