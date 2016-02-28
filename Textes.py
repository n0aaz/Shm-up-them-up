import pygame


pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
gameDisplay = pygame.display.set_mode((display_width,display_height))

def texte_police(texte, police,couleur):
    forme_texte = police.render(texte, True, couleur) #Mise en forme du texte avec la couleur
    return forme_texte, forme_texte.get_rect()

 """Fonction permettant d'afficher un message, a pour entrées le texte,
    la position relative en x et y, la taille et la couleur du texte soit en préréglage, soit en RGB (xRx,xGx,xBx). Elle
    s'occupe de faire appel aux autres fonctions de mise en forme de texte, gérer la police et la taille puis afficher le texte"""
def message_display(text,px,py,taille,couleur):
    taille_texte = pygame.font.Font('ressources/polices/minecraft.ttf',taille) #Mise en forme de la police avec taille
    forme_texte, position_texte = texte_police(text, taille_texte,couleur) #appel a la fonction texte_police
    position_texte.center = ((px),(py)) #position du texte
    gameDisplay.blit(forme_texte, position_texte) #affichage du texte


while True :
    message_display("Test",500,200,115,white)
    pygame.display.update()

