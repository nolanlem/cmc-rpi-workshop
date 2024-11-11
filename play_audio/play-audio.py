import pygame 
pygame.mixer.init()
pygame.mixer.music.load('./audio/piano2.wav')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
	continue

#######

import glob
import board
import time
from adafruit_motorkit import MotorKit
import librosa

kit = MotorKit(i2c=board.I2C())

audiograins = glob.glob('./audio/grains/*.wav')

i = 1
for audiofile in audiograins:
	# load and then play the sound file
	print(f'playing {audiofile} {i}/{len(audiograins)}')
	pygame.mixer.music.load(audiofile)
	pygame.mixer.music.play()

	
	y, sr = librosa.load(audiofile, mono=True) 
	duration = len(y)/sr
	print(f'duration is {duration}') 
	
	time.sleep(duration)	
	#kit.motor3.throttle = 0.9	
	while pygame.mixer.music.get_busy() == True:
		continue

	#kit.motor3.throttle = 0

	i = i + 1 # update incrementer 
