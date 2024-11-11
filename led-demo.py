import RPi.GPIO as GPIO
import time
# Choose which GPIO pin to use
led = 5
# set up GPIO as output
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

# set pin GPIO7 to be "on," turning on the light
GPIO.output(led, 1)
# delays for 1 second, keeping the light on briefly
time.sleep(1)
# set pin GPIO7 to be "off," turning off the light
GPIO.output(led, 0)
# delays for 1 second, keeping the light off briefly
time.sleep(1)

# toggle led on and off 
for i in range(5):
	GPIO.output(led,True)
	print(f'wait {i+1} seconds')
	time.sleep(1)
	GPIO.output(led,False)
	time.sleep(1)


