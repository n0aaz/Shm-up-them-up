import pygame

jaune = [222, 194, 39]
rouge = [255, 64, 0]
blanc = [255, 255, 255]
gris = [128, 128, 128]

class Tir(pygame.sprite.Sprite):
    """ Une classe réservée aux tirs . """
    def __init__(self):
        # On appelle les propriétés des sprite dont découle notre classe
        super().__init__()

        # On va générer notre balle tirée, un ovale jaune de la taille donnée
        self.image = pygame.Surface([12, 6])

        self.couleur = jaune
        self.rect = self.image.get_rect()
        pygame.draw.ellipse(self.image, self.couleur, self.rect)

        self.image.set_alpha(120)

        # Le mode de tir par défaut sera linéaire vers l'est
        self.modetir = "E"
        self.perforant = False

        # Petit interrupteur qui nous servira à savoir si c'est un tir de vaisseau ou de monstre
        self.ennemi = False
        self.etoile = False

        self.vitesse = 12

    def update(self):
        """ Déplacement de la balle selon l'attribut qui lui sera donné """
        # le mode de tir correspond aux points cardinaux d'une boussole, Nord, Sud, Est, Ouest et les entrepoints

        if self.modetir == "N":
            self.rect.y += self.vitesse

        elif self.modetir == "S":
            self.rect.y -= self.vitesse

        elif self.modetir == "E":
            self.rect.x += self.vitesse

        elif self.modetir == "O":
            self.rect.x -= self.vitesse

        elif self.modetir == "NE":
            self.rect.x += self.vitesse
            self.rect.y += self.vitesse

        elif self.modetir == "SE":
            self.rect.x += self.vitesse
            self.rect.y -= self.vitesse

        elif self.modetir == "NO":
            self.rect.x -= self.vitesse
            self.rect.y += self.vitesse

        elif self.modetir == "SO":
            self.rect.x -= self.vitesse
            self.rect.y -= self.vitesse

"""Le tir des ennemis aura les memes caractéristiques que le tir allié mais sera rouge """
class Tirennemi(Tir):
    def __init__(self):
        super().__init__()
        self.couleur = rouge
        self.modetir = "O"
        pygame.draw.ellipse(self.image, self.couleur, self.rect)
        self.ennemi = True

"""Les explosions de vaisseau ressemblent à des tirs mais ne tuent rien, autant les différencier"""
class Explosion(Tir):
    def __init__(self):
        super().__init__()
        self.couleur = blanc
        self.image = pygame.Surface([4, 4])
        pygame.draw.ellipse(self.image, self.couleur, self.rect)
        self.vitesse = 4

"""Les etoiles sont à part, elles se déplacent toujours dans le sens contraire du joueur, et plus lentement
on est dans l'espace quand meme, la perspective existe toujours, même en 2D :) """
class Etoiles(Tir):
    def __init__(self):
        super().__init__()
        self.couleur = gris
        self.image = pygame.Surface([3, 3])
        pygame.draw.ellipse(self.image, self.couleur, self.rect)
        self.vitesse = 1
        self.modetir = "O"
        self.etoile = True
