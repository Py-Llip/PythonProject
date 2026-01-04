import pygame

pygame.init()
pygame.mixer_music.load('C:/Users/felli/Downloads/dancing-in-the-stardust-free-music-no-copyright-203603.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
