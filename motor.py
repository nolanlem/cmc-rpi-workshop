import time 
import board from adafruit_motorkit import 

MotorKit kit = MotorKit(i2c=board.I2C()) 
kit.motor1.throttle = 0.5 # run motor at half speed 
time.sleep(2.0) # wait 2 seconds 
kit.motor1.throttle = 0 # turn off 
