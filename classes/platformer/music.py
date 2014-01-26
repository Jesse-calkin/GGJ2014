import pygame

class Music(object):
	@classmethod
	def play(cls):
		pygame.mixer.music.load("resources/music/music.wav")
		pygame.mixer.music.play()
