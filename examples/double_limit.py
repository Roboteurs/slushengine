'''
This script will travel to two limit switchs on a linear or circular track. The limit switches are at opposite ends of the
actuator. In the test case we have a stepper motor driving a ball screw with a carrage. The ball screw travels to the right limit
switch and then the left limit switch. The program then outputs the distance between limit switches. 

The hardware connection for this circuit is two limit switches connected in series, then connected to the motor 0 limit switch input
the limit switches must both be wired as N.C.

#use cases
*this can be used if  a machine needs calibration before startup
*checking the quality of a mechnical frame and limit switches
*measuring length
'''

import Slush

#system variables
mmPerStep = 0.004873
carrageLength = 55.0 
endPosition = 0

#setup the Slushengine
b = Slush.sBoard()
m = Slush.Motor(0)
m.resetDev()
m.setCurrent(30, 30, 30, 30)

#move the motor to the first limit switch once the switch has arrived set the position as home 
m.goUntilPress(1, 1, 10000)
while m.isBusy():
	continue

#move to the next limit switch
m.goUntilPress(0, 0, 10000)
while m.isBusy():
	pos = m.getPosition()
	if pos != 0:
		endPosition = pos

print ("distance traveled: " + str(endPosition) + " steps")
print ("Length of travel: " + str((endPosition * mmPerStep) - carrageLength) + " mm") 

