# Jeito do professor

# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# import pygame
# pygame.init()
# pygame.mixer.music.load('ex021.mp3')
# pygame.mixer.music.play()
# pygame.event.wait()

# Meu Jeito
# from pygame import mixer # Load the required library
#
# mixer.init()
# mixer.music.load('C:\Projetos Python\Exercicios\ex021.mp3')
# mixer.music.play()

# Jeito nova biblioteca achado na documentação python
# https://pypi.org/project/playsound/
import playsound
playsound.playsound('C:\Projetos Python\Exercicios\ex021.mp3', True)