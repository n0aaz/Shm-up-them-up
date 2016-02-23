import pygame
from pygame.locals import *


class Vaisseau(pygame.sprite.Sprite):
    """ On crée une classe vaisseau , cette classe herite des caractéristiques de la librairie Sprite de Pygame qui va
     Servir a faire une image fixe et mobile du vaisseau"""

    def __init__(self):
        """ Le constructeur de la classe """

        # On appelle le constructeur de la classe parent de notre classe, c'est à dire la classe Sprite de Pygame
        super().__init__()

        # Chargement de l'image du vaisseau ; ne pas oublier convert qui va rendre le fichier manipulable
        # Ne pas oublier de rendre le fond blanc du vaisseau transparent
        self.image = pygame.image.load("vaisseau.png").convert()
        self.image.set_colorkey([255, 255, 255])

        # Taille de l'image du vaisseau, pour faciliter les calculs
        self.taille= self.image.get_size()

        # Appel des coordonnées (taille) de l'image pour en faire les coordonnées du vaisseau
        self.rect = self.image.get_rect()

        # On définit des coordonnées du centre du canon pour faciliter le placement ultérieur
        self.centrecanon = [self.rect.x + self.taille[0] / 2 + 15, self.rect.y + self.taille[1] / 2 - 1]

        # On a trois vies
        self.vie = 3

        # Cette petite variable nous permettra par la suite d'ignorer les collisions quand il est activé
        self.immunite = False

        self.apparition = True
    """ Methode (fonction) de la classe pour le mouvement du vaisseau qui suivra celui de la souris"""

    def update(self):
        # On demande la position de la souris et on la
        # stocke dans une liste de deux valeurs x et y
        position = pygame.mouse.get_pos()

        # Actualisation de la position calculée du centre du canon
        self.centrecanon = [self.rect.x + self.taille[0] / 2 + 15, self.rect.y + self.taille[1] / 2 - 1]

        # La position du vaisseau sera donc celle de la souris
        if self.immunite == False:
            self.rect.x = position[0]
            self.rect.y = position[1]

    def mort(self):

        # Lorsque la mort est demandée , on pert une vie mais on devient immunisé pour éviter d'en perdre plusieurs
        self.vie -= 1
        self.immunite = True
        self.image.set_alpha(0)

        # Et est joué le bruit d'explosion
        #explosion = pygame.mixer.Sound("explosion.ogg")
        #explosion.play()

    def cligno(self):

        # On fait clignoter l'image du vaisseau en faisant varier la transparence de ce dernier
        transparence = self.image.get_alpha()
        if self.apparition == True:
            transparence+=4
            if transparence > 255:
                self.apparition = False
        else:
            transparence-=4
            if transparence < 10:
                self.apparition = True
        self.image.set_alpha(transparence)