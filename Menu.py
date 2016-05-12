import pygame
"""Création d'une classe appelée menu"""
class texte_menu:

    #Etat de la condition de passage de la souris
    passage = False

    #Définition de la classe
    def __init__(self, texte, pos):
        self.texte = texte
        self.pos = pos
        self.mise_en_page()
        self.dessin()


    #Fonction de mise en forme du texte
    def rendu_texte(self):
        self.rend = menu_font.render(self.texte, True, self.couleur())

    #Choix de la couleur en fonction de la variable de passage pour permettre un luminessance lors du passage de la souris
    def couleur(self):
        if self.passage:
            return (255, 255, 255)
        else:
            return (100, 100, 100)
    #Mise en page du texte dans l'écran
    def mise_en_page(self):
        self.rendu_texte()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

    #Fonction de dessin du menu sur l'écran
    def dessin(self):
        self.rendu_texte()
        screen.blit(self.rend, self.rect)

###################PROGRAMME A INTEGRER DANS LE PROGRAMME FINAL #######################################################

########## Pour le programme de test, sera enlevé par la suite #######
pygame.init()
screen = pygame.display.set_mode((1080,720))
##########

#Choix de la police
menu_font = pygame.font.Font("ressources/polices/Minecraft.ttf", 40)
#Configuration des différentes options du menu
options = [texte_menu("JOUER", (300, 205)), texte_menu("OPTIONS", (300, 255)),
           texte_menu("MEILLEURS SCORES", (300, 305)),texte_menu("CREDITS", (300, 355))]
while True:
    pygame.event.pump()
    screen.fill((0, 0, 0))
    for option in options:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.passage = True
        else:
            option.passage = False
        option.dessin()
    pygame.display.update()
