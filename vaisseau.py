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
        self.image.set_colorkey(255, 255, 255)

        # Appel des coordonnées (taille) de l'image pour en faire les coordonnées du vaisseau
        self.rect = self.image.get_rect()

        # On a trois vies
        self.vie = 3

        # Cette petite variable nous permettra par la suite d'ignorer les collisions quand il est activé
        self.immunite = False

    """ Methode (fonction) de la classe pour le mouvement du vaisseau qui suivra celui de la souris"""

    def mouvement(self):
        # On demande la position de la souris et on la
        # stocke dans une liste de deux valeurs x et y
        position = pygame.mouse.get_pos()

        # La position du vaisseau sera donc celle de la souris
        self.rect.x = position[0]
        self.rect.y = position[1]

    def mort(self):

        # Lorsque la mort est demandée , on pert une vie
        self.vie -= 1

        # Et est joué le bruit d'explosion
        explosion = pygame.mixer.Sound("explosion.ogg")
        explosion.play()

        # Etre immortel pendant 5s avant de faire réapparaitre le vaisseau, laisser du répit au joueur
        """mortel= pygame.USEREVENT+1
        pygame.time.set_timer(mortel, 5000)
        for event in pygame.event.get():
            while event.type != mortel:
                self.immunite = True""" # En cours de travail

