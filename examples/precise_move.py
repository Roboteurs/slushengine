"""
Title: Precise Motor Move

Description: This example will show the diffrent powerful features of the SlushEngines
smart driving capabilities. Please read comments to better understand what the motor is
doing. All pauses in the program can be removed. They are placed to better show the difrence
between commands. 

Note: This example is dependant on your type of motor and power supply. If you find 
you motor skipping steps you may need to slow it down a bit. 

Note: It is recommended to place an object or peice of tape on the end of your motors shaft.
this will allow you to see the ability of the driver. You may also run the program TOP to
see the processor load during operation

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

#wait for the move to be not busy
while(Motor.isBusy()):
	continue

#move the motor at a new microstepping setting
print("-> moving the motor at 128 Step/Step microstepping")
Motor.setMicroSteps(128)
Motor.move(-100000)
while(Motor.isBusy()):
	continue
print("-> motor is free move it as you like, you have 5 seconds!")
Motor.free()
time.sleep(5)

#set the current position to home using the drivers internal logic
print("-> setting the current position to home")
Motor.setAsHome()
time.sleep(1)

#moving to a position with refrence to home
print("-> moving 200000 steps from home position")
Motor.goTo(200000)
while(Motor.isBusy()):
	continue
time.sleep(1)

#moving to a position with refrence to home
print("-> moving -300000 steps from home position")
Motor.goTo(-300000)
while(Motor.isBusy()):
	continue
time.sleep(1)

#run the motor for a short period of time
print("-> running the motor to random position")
Motor.run(1, 100)
time.sleep(5) #can be changed to any value

#return the motor to home
print("-> returning the motor to home position")
Motor.goHome()

#free the motor
while(Motor.isBusy()):
	continue
Motor.free()






