''' Source Refrence: https://github.com/ameyer/Arduino-L6470/blob/master/L6470/L6470.cpp
'''

__author__ = 'mangokid'

from Slush.Board import *
import quick2wire.i2c as i2c
import binascii
import math


class Temprature(sBoard):

    def __init__(self):
        """ basic init functions for the temprature module
        """
        self.address = 0x36
        self.initSensor()

    def initSensor(self):
        """ initalizes the first channel if the MAX1164 device in single
        endded mode with vdd as ref
        """
        with i2c.I2CMaster(1) as bus:
            bus.transaction(i2c.writing_bytes(self.address, 0x8a ))
            bus.transaction(i2c.writing_bytes(self.address, 0x01 ))    

    def getTempRaw(self):
        """ gets the raw hex values from the i2c device
        """
        with i2c.I2CMaster(1) as bus:
            x = (bus.transaction(i2c.reading(self.address, 2)))
            h = int(binascii.hexlify(x[0]), 16)
            
            #mask for 10 bit ADC
            return (h & 0b0000001111111111)

    def calcTemp(self, tempraw):
        """ calculate temprature with Steinhart-Hart equations paramters
        are rough defualts for 50k resistor
        """ 
        POTENTIAL_DIVIDER_RESISTOR = 100000
        THERMISTOR_B_VALUE = 3950
        THERMISTOR_REF_TEMP = 298.15
        THERMISTOR_REF_RESISTANCE = 50000

        voltage = float(tempraw) / 1024 * 5
        resistance = POTENTIAL_DIVIDER_RESISTOR / (5 / voltage - 1)
        temp = 1 / (1/THERMISTOR_REF_TEMP + math.log(resistance / THERMISTOR_REF_RESISTANCE) / THERMISTOR_B_VALUE)
        #print "Temperature is: %f K, (%f degC)" % (temp, temp-273.15)
    
        return temp-273.15

    def getTemprature(self):
        """ return the temprature at the NTC junctino
        """
        return self.calcTemp(self.getTempRaw())

