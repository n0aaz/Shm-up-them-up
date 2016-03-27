import pygame
class  textes(pygame.sprite.Sprite) :
    def __init__(self):
        self.texte = "texte"
        self.taille = 115
        self.surlignage = True
        self.couleur = (255, 100, 100)
        self.image = message_display(self.texte,self.taille,self.couleur)


    def texte_police(texte, police,couleur):
        forme_texte = police.render(texte, True, couleur) #Mise en forme du texte avec la couleur
        return forme_texte,

    def message_display(text,taille,couleur):
        taille_texte = pygame.font.Font('ressources/polices/minecraft.ttf',taille) #Mise en forme de la police avec taille
        forme_texte= texte_police(text, taille_texte,couleur) #appel a la fonction texte_police
        return forme_texte

    def update(self):
        if self.surlignage:
            self.couleur = (255, 255, 255)
        else:
            self.couleur = (100, 100, 100)

        self.image = message_display(self.texte,self.taille,self.couleur)


