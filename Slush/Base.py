#!/usr/bin/python3

#Slush system includes
import time
import os
import sys

#include the spi dev drivers and check if spi is enabled
try:
  import spidev as spidev
except ImportError:
  raise ImportError("Cannot load spidev library")

#include the i2c drivers and check if i2c is enabled
try:
  import quick2wire.i2c as i2c
  from quick2wire.parts.mcp23017 import MCP23017
  from quick2wire.parts.mcp23x17 import In, Out
  from quick2wire.i2c import I2CMaster, writing_bytes, reading
  from contextlib import closing
except ImportError:	
  raise ImportError("Cannot load i2c library (quick2wire)")

#include the gpio drivers
try:
  import RPi.GPIO as gpio
except ImportError:
  raise ImportError("Cannot load the Raspberry Pi GPIO drivers")

#include SMbux drivers
try:
    import smbus2 as SMBus
except ImportError:
    raise ImportError("Cannot Load SMBus library")