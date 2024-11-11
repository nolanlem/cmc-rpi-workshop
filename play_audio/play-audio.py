import pygame 
pygame.mixer.init()
pygame.mixer.music.load('../../music/piano2.wav')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
	continue
