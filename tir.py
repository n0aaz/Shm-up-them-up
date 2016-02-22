import pygame

jaune = [222, 194, 39]


class Tir(pygame.sprite.Sprite):
    """ Une classe réservée aux tirs . """
    def __init__(self):
        # On appelle les propriétés des sprite dont découle notre classe
        super().__init__()

        # On va générer notre balle tirée, un ovale jaune de la taille donnée
        self.image = pygame.Surface([6, 3])
        pygame.draw.ellipse(self.image, jaune, self.rect)

        self.rect = self.image.get_rect()

        # Le mode de tir par défaut sera linéaire
        self.modetir = "droit"

    def mouvement(self):
        """ Déplacement de la balle selon l'attribut qui lui sera donné """
        if self.modetir == "droit":
            self.rect.x += 4

        if self.modetir == "diagonalehaut":
            self.rect.x += 4
            self.rect.y += 4

        if self.modetir == "diagonalebas":
            self.rect.x += 4
            self.rect.y -= 4

        if self.modetir == "arriere":
            self.rect.x -= 4
