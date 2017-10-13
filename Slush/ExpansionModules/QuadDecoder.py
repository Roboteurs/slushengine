from Slush.Board import *
import math

class encoder(sBoard):
	
	DEVICEADDR = 0x3c
	homePos = 0

	def initDevice(self, encoderRes, gRatio):
		"""This function initiates the encoder properties. This function should be called once at
		the beginning of your program. Passing nothing into this function will initialize it
		with the defaults
		"""

		#setup some encoder parameters	
		self.encoderRes = (encoderRes * 4)
		self.gRatio = gRatio

		#check if there is an encoder module connected
		if self.isConnected():
			sucess = 1
		else:
			sucess = 0
		
		return sucess

	def setHome(self, offset):
		"""Sets the internal position counter of the encoder add-on board to zero. When the
		device is position is queried in the future it will be with reference to this position.
		"""
		encoder.homePos = self.getPosition()
		pass

	def resetDevice(self):
		"""Resets the device to all of its default values. This will also reset the position of the
		encoder and any other user set registers. This command is not needed during
		normal device operation. The device will reset immediately and requires no time to
		reboot.
		"""
		pass

	def checkStatus(self):
		"""This function will get the status of the add-on board. This is used to check if the
		device has detected a fault. A fault can be caused by a disconnected wire, poor
		signal or signal interference. It is recommended to check the status once at the
		beginning of you program.
		"""
		pass

	def getPosition(self):
		"""This gets the positon of the encoder relative to the zero set during the get home
		command or the devices state on power up.
		"""
		pos = 0
		for i in range (0, 4):
			pos += self.readReg((0x04 + i)) << 8*i

		if pos > (math.pow(2,32) / 2):
			pos = pos - (math.pow(2,32))

		#calculate postition relative to the home pos
		pos = pos - encoder.homePos

		return int(pos)

	def getAngle(self):
		"""Calculates the angle of the rotor in degrees relative to the zero position of the motor.
		This function requires that the number of counts per revolution is set in The
		initialization.
		"""
		countPos = self.getPosition()

		#calculate the number of revolutions and multiply by 360. 
		angle = (countPos/self.encoderRes) * 360.0

		return angle

	def getDirection(self):
		"""Returns the direction of travel of the encoder. If the encoder is not moving it will
		return the last know direction of travel
		"""
		pass

	def isConnected(self):
		"""Checks if the enceder device is actually connected to a slush module
		"""
		return 1

	def readReg(self, register):
		with i2c.I2CMaster(1) as bus:
            		return bus.transaction(i2c.writing_bytes(encoder.DEVICEADDR, register),i2c.reading(encoder.DEVICEADDR, 1))[0][0]



