import pygame

from pygame.locals import *

"""Création d'une classe appelée menu pour afficher les données du menu"""

class texte_menu :

    #Définition d'une variable de passage au dessus de l'espace choisi
    passage = False

    #Création d'une classe texte :
    def __init__(self, texte, position):
        self.texte = texte
        self.position = position
        self.alignement()
        self.draw()

    def draw(self):
        self.typetexte()
        fenetre.blit(self.rend, self.rect)

    def typetexte(self):
        self.rend = pygame.font.Font(None, 40).render(self.texte, True, self.couleur())

    def couleur(self):
        if self.passage:
            return (255, 255, 255)
        else:
            return (50, 50, 100)

    def alignement(self):
        self.typetexte()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.position
