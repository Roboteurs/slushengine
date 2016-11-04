"""
Title: Motor Settings

Description: This example will iterate through a number of diffrent stepper motor 
settings. This program is intended to show some of the diffrent configurations the
motor is capable of. 

Note: This example is dependant on your type of motor and power supply. If you find 
you motor skipping steps you may need to slow it down a bit.

"""
#import the required module
import Slush
import time

#initalizes the board and all its functions
SlushEngine = Slush.sBoard()

#initalizes the motor on the board
Motor = Slush.Motor(0)
Motor.resetDev()
Motor.setCurrent(20, 20, 20, 20)

#run the motor with the defulat settings
print("Running the motor at 100 Steps/Second")
Motor.run(1, 100)
time.sleep(2)

#disable motor driving power
print("Drive disabled, motor can now free spin")
Motor.free() 
time.sleep(5) 

#move the motor 20000 steps from its current position at the deault settngs
print("Moving the motor 100000 steps in reverse")
Motor.move(-100000)

#wait for the move to finish
while(Motor.isBusy()):
	continue

#move the motor with some new parameters
print("Slowly moving motor in the oposite direction")
Motor.setAccel(10)
Motor.setDecel(10)
Motor.setMaxSpeed(2000)
Motor.move(20000)

#wait for the move to finish
while(Motor.isBusy()):
	continue

#move the motor at a new microstepping setting
print("move the motor at 1 Step/Step microstepping")
Motor.setMicroSteps(1)
Motor.move(200)
