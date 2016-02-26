import pygame
import tir
import math

jaune = [222, 194, 39]
noir = [0, 0, 0]


class Bonusplus(pygame.sprite.Sprite):
    """ Une classe réservée aux tirs . """
    def __init__(self):
        # On appelle les propriétés des sprite dont découle notre classe
        super().__init__()
        self.bonus = True
        self.ennemi = False

        # Génération du bonus
        self.image = pygame.image.load("bonusplus.png").convert()
        self.image.set_colorkey([255, 255, 255])
        self.rect = self.image.get_rect()

        # Interrupteurs d'état pour savoir quel bonus activer
        self.plus = True
        self.rond = False
        self.etoile = False

        self.naissance = 0
        self.compteur = 0

    def update(self):
        """ Déplacement """
        # Déplacement sinusoïdal
        self.compteur += 50
        self.rect.y = self.compteur / 10 % 1600
        self.rect.x = math.sin(self.compteur / 10 % 1600 / 100)*200 + self.naissance


class Bonusrond(Bonusplus):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bonusrond.png").convert()
        self.image.set_colorkey([255, 255, 255])

        self.rond = True
        self.plus = False
