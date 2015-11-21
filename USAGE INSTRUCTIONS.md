SlushEngine Usage Instructions
==============================

Using the SlushEngine Python software package is relativley simple once all of the required packages have been installed. Before powering a SlushEngine device please ensure that you read the hardware notes listed below.

Hardware Setup
--------------

1. Check for correct polarity of the power conection to the SlushDevice
2. Check the voltage to the device is within its operating range
3. Check the oreientation of the connectors between the Raspberry Pi and the SlushEngine device
4. Have some method of communication with the Raspberri Pi setup. (ie. SSH Terminal, Screen & Keyboard, etc...)


Getting Started
---------------

- Power on the device and wait for the Pi to boot
- Open a Python 3 terminal (this can be done from a console by typing Python3)
- In the terminal enter the following command
  $ import Slush
- This will import the Slush module and test and configure the connected devices

Moving a Motor
--------------

When the Slush module is imported it sets some basic defaults on the motor control hardware. These defaults should allow basic usage of a stepper motor in test conditions. To further improve the operation of the motor these settings can be taylor from within the code.

Import the required module as done before. This may take ~100ms depending on the device connected

> $ import Slush

Then we have to create the board object. This object can be later used to access other features of the SlushEngine other than just the motors

> $ SlushEngine = Slush.sBoard()

Then we need to create the motor object. Depending on the Slush device in use multiple motor objects can be created in the same way. Each object can be access indicidually for specific control of a motor.

> $ Motor = Slush.Motor(0)

Finally to move the motor a simple command is passed to the motor obect that was created. This command will move the motor a specific number of steps. The direction of motion is based on the signage of the intager passed to the object.

> $ Motor.move(-100000)

Changing Motor Settings
-----------------------

At any point during operation when a motor is not busy the setting can be changed to alter the motors preformance. An example might be changing the motors microstepping level to allow faster motion. This is done by changing the propoerties of the particular motor object. Each initalized motor object can have diffrent settings from others on the same device.

For example if we wanted to change the motors microstep settings

> $ Motor.setMicroSteps(1)

At the moment the other settings are not all documented although they do exist in the code. You can browse the Example code for some examples of other settings that may be changed. The settings are all documented in the code under Examples.
