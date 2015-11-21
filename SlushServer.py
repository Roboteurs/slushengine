"""
Title: SlushServer

The Raspberry Pi allows us the oportunity to network the Raspberry Pi. I created a quick and simple way to allow this to be realized. This program is run on the Raspberry Pi attached to the Slush device. If your Raspberry Pi is connected to a local network you will be able to access it and send commands over TCP/IP. This can be done from Python, Putty, Java, Labview, etc...

How it works: When a command is sent over the socet to port 1248 it is received and interpreted using the "exec" command. As long as the commands are in the format of MotorX then it will operate correctley and return values as well.

This program is very Beta and I understand there are a lot of holes in it. If you have any sugjestions please post an issue.

"""

import Slush
import socket
import sys
import time

#setup the socket and listen
slush_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
slush_socket.bind(('0.0.0.0', 1248))
slush_socket.listen(1)
slush_socket.setblocking(0)

#initalize the board in case poeple are using peripherals
SlushEngine = Slush.sBoard()

#initalize all the motors
Motor1 = Slush.Motor(0)
Motor2 = Slush.Motor(1)
Motor3 = Slush.Motor(2)
Motor4 = Slush.Motor(3)

#initalize the temprature sensor
TempSensor = Slush.Temprature()

#run this loop. It should never error but its very beta and basic
while True:
    buf = []

    try:
        connection, address = slush_socket.accept()
        #print ("new connection created")
        buf = connection.recv(1024)

        if buf != [0]:
            if len(buf) > 0:
            	print (buf)
            try:
                exec (buf)
                print (str(retval))
                if retval != None:
                    connection.send(str(retval).encode())

            except:
                print("Invalid Command")

        connection.close()

    except:
        #print ("Something failed")
        pass

    time.sleep(0.01)
    
 
    	




