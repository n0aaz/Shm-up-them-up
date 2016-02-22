import pygame
import random

""" On appelle nos classes définies dans des fichiers à part"""
import vaisseau
import tir

# Initialisation de pygame
pygame.init()

# Taille de l'écran , on prend un ratio de 16/9
largeur = 80*16
hauteur = 80*9
fenetre = pygame.display.set_mode([largeur, hauteur])


# Initialisation de clock pour gérer la vitesse de rafraichissement
clock = pygame.time.Clock()

arret = False


###############################################Programme principal
while not arret:
    # On stoppe le programme si l'utilisateur quitte
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Nettoyage de l'écran
    screen.fill([0,0,0])

    # Affichage de tout
    pygame.display.flip()

    # Quasiment tous les écrans sont limités à 60hz de rafraichissement
    # Pourquoi vouloir aller plus vite?
    # Limite de rafraichissement à 60 fois par seconde
    clock.tick(60)

pygame.quit()
﻿