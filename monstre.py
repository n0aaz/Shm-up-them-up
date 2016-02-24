import pygame
import math
from pygame.locals import *

class Monstre(pygame.sprite.Sprite):
    """On crée une classe appelée Monstre. Elle contient les caractéristiques SPRITE de Pygame pour avoir des monstres mobiles sur
        un fond fixe"""
    def __init__(self):
        """Construction de la classe"""
        # Appel de la fonction de création de la classe
        super().__init__()
        # Chargement de l'image du monstre
        self.image = pygame.image.load("monstre.png").convert()
        # Affichage arrière plan image transparent
        self.image.set_colorkey([255, 255, 255])

        # # # # # # # # # #

        # Mesure de la taille de l'image
        self.taille= self.image.get_size()

        # Position générale
        self.rect = self.image.get_rect()
        # Position du centre
        self.centremonstre = [self.rect.x / 2, self.rect.y / 2 ]

        # # # # # # # # # #
        self.modedeplacement="D"
        # Position de naissance
        self.compteur=0
        self.naissance = 0
        self.etoile=False

    def update(self):
        """Ce sera appelé à chaque image"""
        if self.modedeplacement == "D":
            self.rect.x -=5
        elif self.modedeplacement == "S":
            self.compteur += 50
            self.rect.x = 1280-(self.compteur / 10 %1600)
            self.rect.y = math.sin(self.compteur / 10 % 1600 / 50)*100 + self.naissance
        elif self.modedeplacement == "R" : ##Ne fonctionne pas poru le moment,
            self.rect.x -=5
            self.rect.y +=2
            if self.rect.x - 5 <0 or self.rect.x +5 >720 :
                self.rect.x +=5
            if self.rect.y -2 <0 or self.rect.y +2 >720 :
                self.rect.y -=2



