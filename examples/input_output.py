"""
Title: Input Output

Description: This program will read the inputs on the SlushEngine expansion IO. During this program you
may apply 3.3V or ground to any of the pins to observe there change. This program can be modified to 
include motor controls based on the inputs and outputs. 

"""
#import the required module
import Slush
import time

#initalizes the board and all its functions
SlushEngine = Slush.sBoard()

while(1):
	
	#reads pin A0 and prints the value
	print("Pin A0: " + str(SlushEngine.getIOState(0, 0)))

	#reads the value of pin B0 and sets an LED based on the reading connected to A7
	if SlushEngine.getIOState(1, 0) == 1:
		SlushEngine.setIOState(0, 7, 1)
	else:
		SlushEngine.setIOState(0, 7, 0)

	time.sleep(1)



