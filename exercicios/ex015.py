#faça um programa em python que abra e reproduza o audio de um arquivo mp3.
import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(r'C:\Users\Leon\Documents\VSCode\Projetos\Curso em video\ex021.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.myxer.music.play()
while pygame.myxer.music.get_busy():
    pygame.time.Clock().tick(10)
