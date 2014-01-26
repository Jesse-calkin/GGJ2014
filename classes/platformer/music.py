import pygame

class Music(object):
	@classmethod
	def play(cls):
		pygame.mixer.music.load("../../resources/music/music.ogg")
		pygame.mixer.music.play()
