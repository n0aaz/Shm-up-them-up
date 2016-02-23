import pygame
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

        # Coordonnées du monstre dans le plan
        self.taille= self.image.get_rect()
        # Position générale
        self.rect = self.image.get_rect()
        # Position du centre
        self.centremonstre = [self.rect.x / 2, self.rect.y / 2 ]


        # # # # # # # # # #
        self.modedeplacement="D"

        self.etoile=False

    def update(self):
        """Ce sera appelé à chaque image"""
        if self.modedeplacement == "D":
            self.rect.x -=5




