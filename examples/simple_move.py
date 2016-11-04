'''
This python script will initalize a motor and move it back and forth for a number of steps
- this program was tested on a SlushEngine Lite & SlushEngine Model X
- Tested with a Nema 17 @ 24v & Nema 23 & 18v
- Motor will draw approx 0.5A 
'''

import Slush

#the number of steps we want to be moving
stepmove = 300000

#setup the Slushengine
b = Slush.sBoard()
axis1 = Slush.Motor(0)
axis1.resetDev()
axis1.setCurrent(50, 50, 50, 50)

#move the motor in one direction and wait for it to finish
while(axis1.isBusy()):	
	continue
axis1.move(stepmove)

while(axis1.isBusy()):
	continue
axis1.move(-1 * stepmove)
	
#when these operations are finished shut off the motor
while(axis1.isBusy()):
	continue
axis1.free()
