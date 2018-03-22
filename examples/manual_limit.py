'''
the example uses the move command and the manual limit switch check command. It moves the motor and then checks the limit switch.
this can be used to do fine manual homing
'''

import Slush

#setup the motor
b = Slush.sBoard()
m = Slush.Motor(1)
m.resetDev()
m.setLimitHardStop(0)
m.setCurrent(50, 50, 50, 50)
m.setMaxSpeed(100)

#move until the limit switch is pressed
while m.getSwitch():
	m.move(100)
