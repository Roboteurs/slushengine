__author__ = 'mangokid'

import Slush.Boards.SlushEngine_ModelX as SLX
from Slush.Base import *

class sBoard:
  chip = 0

  def __init__(self):
    """ initalize all of the controllers peripheral devices
    """
    self.initSPI()
    self.initGPIOState()
    self.initI2C()    
	       
  def initGPIOState(self):
    """sets the default states for the GPIO on the slush modules. *This
    is currently only targeted at the Raspberry Pi. Other target devices
    will be added in a similar format.
    """  
    gpio.setmode(gpio.BCM) 

    #common motor reset pin
    gpio.setup(SLX.L6470_Reset, gpio.OUT)
    
    #chip select pins, must all be low or SPI will com fail
    gpio.setup(SLX.MTR0_ChipSelect, gpio.OUT)
    gpio.setup(SLX.MTR1_ChipSelect, gpio.OUT)
    gpio.setup(SLX.MTR2_ChipSelect, gpio.OUT)
    gpio.setup(SLX.MTR3_ChipSelect, gpio.OUT)
    gpio.setup(SLX.MTR4_ChipSelect, gpio.OUT)
    gpio.setup(SLX.MTR5_ChipSelect, gpio.OUT)
    gpio.setup(SLX.MTR6_ChipSelect, gpio.OUT)
    gpio.output(SLX.MTR0_ChipSelect, gpio.HIGH)
    gpio.output(SLX.MTR1_ChipSelect, gpio.HIGH)
    gpio.output(SLX.MTR2_ChipSelect, gpio.HIGH)
    gpio.output(SLX.MTR3_ChipSelect, gpio.HIGH)
    gpio.output(SLX.MTR4_ChipSelect, gpio.HIGH)
    gpio.output(SLX.MTR5_ChipSelect, gpio.HIGH)
    gpio.output(SLX.MTR6_ChipSelect, gpio.HIGH)

    #IO expander reset pin
    gpio.setup(SLX.MCP23_Reset, gpio.OUT)
    gpio.output(SLX.MCP23_Reset, gpio.HIGH)

    #preforma a hard reset
    gpio.output(SLX.L6470_Reset, gpio.LOW)
    time.sleep(.1)
    gpio.output(SLX.L6470_Reset, gpio.HIGH)    
    time.sleep(.1)  
  
  def initSPI(self):
    """ initalizes the spi for use with the motor driver modules
    """    
    sBoard.spi = spidev.SpiDev()
    sBoard.spi.open(0,0)
    sBoard.spi.max_speed_hz = 100000
    sBoard.spi.bits_per_word = 8
    sBoard.spi.loop = False
    sBoard.spi.mode = 3
    
  def initI2C(self):
    """ initalizes the i2c bus without relation to any of its slaves
    """
    with closing(i2c.I2CMaster(1)) as bus:
        self.chip = MCP23017(bus, 0x20)
        self.chip.reset()

  def deinitBoard(self):
    """ closes the board and deinits the peripherals
    """
    gpio.cleanup() 

  def setIOState(self, port, pinNumber, state):
    """ sets the output state of the industrial outputs on the SlushEngine. This
    currentley does not support the digitial IO
    """
    with closing(i2c.I2CMaster(1)) as bus:
        industrialOutput = self.chip[port][pinNumber]
        industrialOutput.direction = Out
        industrialOutput.value = state

  def getIOState(self, port, pinNumber):
    """ sets the output state of the industrial outputs on the SlushEngine. This
    currentley does not support the digitial IO
    """
    with closing(i2c.I2CMaster(1)) as bus:
        industrialInput = chip[port][pinNumber]
        industrialInput.direction = In
        industrialInput.pull_up = True
        state = industrialInput.value

    return state
  
  def readInput(self, inputNumber):
    """ sets the input to digital with a pullup and returns a read value
    """
    with I2CMaster(1) as master:
        master.transaction(writing_bytes(0x17, inputNumber + 8, 0x00))
        result =  master.transaction(writing_bytes(0x17, inputNumber + 20), reading(0x17, 1))
        return result[0][0]
  def setOutput(self, outputNumber, state):
    """ sets the output state of the IO to digital and then sets the state of the 
    pin        
    """
    with I2CMaster(1) as master:
        master.transaction(writing_bytes(0x17, outputNumber, 0x00))
        master.transaction(writing_bytes(0x17, outputNumber + 12, state))
  def readAnalog(self, inputNumber):
    """ sets the IO to analog and then returns a read value (10-bit)        
    """
    with I2CMaster(1) as master:
        master.transaction(writing_bytes(0x17, inputNumber + 8, 0x01))
        result1 =  master.transaction(writing_bytes(0x17, inputNumber + 20), reading(0x17, 1))
        result2 =  master.transaction(writing_bytes(0x17, inputNumber + 20 + 4), reading(0x17, 1))
        return (result1[0][0] << 2) + result2[0][0]
  def setPWMOutput(self, outputNumber, pwmVal):
    """ sets the output to PWM (500Hz) and sets the duty cycle to % PWMVal/255        
    """
    with I2CMaster(1) as master:
        master.transaction(writing_bytes(0x17, outputNumber, 0x01))
        master.transaction(writing_bytes(0x17, outputNumber + 12, pwmVal))


    
