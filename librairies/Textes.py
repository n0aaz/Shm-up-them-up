import pygame

class Textes(pygame.sprite.Sprite):
    def __init__(self, font_path, font_size):
        #Création de la classe
        pygame.sprite.Sprite.__init__(self)
        # Définition de la police
        self.police = pygame.font.Font(font_path, font_size)
        # Choix de la couleur
        self.couleur = (100,100,100)
        # Choix du texte
        self.texte = "texte"
        # Choix des contours
        self.rerender(5,5)
        # Variable de surlignage
        self.surligne = False
        # Positionnement du centre
        self.centre = 2

    def update(self):
        #position = pygame.mouse.get_pos()
        #self.rect.x = position[0]
        #self.rect.y = position[1]

        if self.surligne == True :
            self.couleur= (255,255,255)
        else :
            self.couleur=(100, 100,100)

        self.rendu(self.rect.x,self.rect.y)

    def print_texte(self, texte_s, x, y):
        self.texte = texte_s
        self.rendu(x,y)
    def rendu(self, x, y):
        self.image = self.police.render(self.texte, 0, self.couleur)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.taille = self.image.get_size()
        self.centre = self.taille[0]/2
