###Motor Control Commands
This page describes many of the commands that can be used to control the SlushEngine motor drivers. All of the commands are described with there input parameters and some examples are given. Please note that the motor setup and initalization is negated in most examples.

#### Some Quick Fundamentals about Stepper Motors
If you do not work with stepper motors this might be a quick and easy read to help understand what many of the below commands will do in the real world. A stepper motor is a rotational electron magnetic device that is not self commutating. By applying controlled alternating current to the motors windings we can make the motor step along. 

![Stepper Motor GIF from Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/StepperMotor.gif/200px-StepperMotor.gif)

A stepper motors resolution (or number of steps per revolution) is mechnically defined by how many poles there are in the motor. Most stepper motors that are commonly avalible have 200 steps per revolution, or 1.8 degrees of travel per step. We employ what is referd to as microstepping to dived the current bewteen poles to produce a lower torque higher resolution step count. In the case of the SlushEngines this can be (1/2 - 1/128). This gives us an effective resolution of 0.014 degrees per step.

The Slushengine system does all of the work of driving a stepper motor for you. There is no need to understand how to control step rate, decay mode, micro stepping and direction change (but it is interesting stuff if you want to learn). The basics you should know about how the SlushEngine controls motors are as follows. 

* All motion is refered to in number of steps and seconds
* The SlushEngine always keeps track of every motors position there is no need to track it in software
* The SlushEngine cannot track the motors position when the motor is off
* The SlushEngine has preprogrammed acceleration and deceleration curves that are used when controlling the motor. These can be changed.
* The direction your motor moves is dependant on how it is wired.
* The SlushEngine has integrated protection features that are covered in the settings section

**myMotor.isBusy()**

-> return 0,1

checks if the motor is busy. If a motor is in the middle of a goto or move command this will return 1. If the motor is executing a run command and has finished accelerating the motor will not be busy.
```python
''' Here we are waiting for motor to finish a task and then we will start the next one. '''
myMotor.Move(-10000)
while myMotor.isBusy():
	continue
myMotor.Move(10000)
```

**myMotor.waitMoveFinish()**

similar to the isBusy command this command waits for a motor to not be busy. Be careful using this command becuase it will block your program and wait for the motor to finish. 

**myMotor.run(dir, spd)**
-> dir: direction of travel (0,1)
-> spd: speed, steps/sec (0.015 - 15625)
runs the motor forever at a continues rpm. This command will start by running the motor allong the set acceleration path and then it will run continusly until a stop command is issued.
```python
''' The example of an engine simulator we want to spin a motor at 900 rpm to give an idle. This simulation does not require microstepping to it is turned off. '''
requestRPM = 900
myMotor.setMicroSteps(1)
myMotor.run(1, 900/60 * 200)
```

**myMotor.move(nStep)**

-> nStep: number of steps (+-4194303)

move some number of steps relative to your current motor position. When this command is issued the motor will begin to accelerate to its max speed, run and then decelerate to its min speed or 0. During this operation the motor will be busy. 
```python
'''In a linear timing pulley belt system -> Timing pulley:22 Teeth, Pitch 2mm, MicroStepping: 128 '''
distanceToTravel = 0.10 #100 millimeters is the distance we want to travel
stepsPerMili = (200 * 128)/(22*2) #number of steper per rev / number of mm per revolution
myMotor.Move(int(distanceToTravel * stepsPerMili))
```

**myMotor.goTo(pos)**

-> pos: number of steps from home (+-4194303)

much like the move command this function will move the motor to a position relative to the home position. The home position is set when the motor turns on and can be set with the setAsHome command. This function is very useful and will be the core of most motion systems. This function respects microstepping and will follow acceleration and deceleration curves.
```python
''' this program assumes that you have just hit a limit switch or some kind of sensor and you want to zero your system. It will set the current position to home. Move forward and then move back. '''
myMotor.setAsHome()
myMotor.goTo(10050)
myMotor.waitMoveFinished()
myMotor.goHome()
```

**myMotor.goHome()**

this will tell the motor to go to the home position. This is the position that is set when the motor turns on or is set by the setAsHome command. During the motion of this command the motor will be busy. 

**myMotor.setMark(mark)**

->mark: number of steps(+-4194303)

sets a mark for the stepper motor to move to. No motion will occure when this command is issued. 

**myMotor.goMark()**

the motor will travel the the mark point. The motor will be busy during this operation. The motor will respect all accerleration and decceleration. 

**myMotor.setAsHome()**

this will set the position control register for the motor to zero and it will set the home position to the current position of the motor. 

**myMotor.softStop()**

brings the motor to a stop using the deceleration pattern. This is handy to prevent vibration and step loss. 

**myMotor.hardStop()**

imeditaley stops the motion of the motor
```python
''' In this example we are going to run the motor for a random amount of time and then hard stop it. This situation is not practicle it just demonstrates the hard stop function '''
import time
import random

myMotor.run(1, 400)
time.sleep(random.randint(0, 60))
myMotor.hardStop()
```

**myMotor.softFree()**

slows the motor down using the deceleration setting and then removes power to the motor once it has stopped. At this point the motor will not be braked and it will spin freely.

**myMotor.free()**

this will remove all power from the motor. The motor will spin freely.
