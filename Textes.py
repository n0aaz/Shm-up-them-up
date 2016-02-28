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

def message_display(text,po,taille,couleur):
    taille_texte = pygame.font.Font('ressources/polices/minecraft.ttf',taille) #Mise en forme de la police avec taille
    forme_texte, position_texte = texte_police(text, taille_texte,couleur) #appel a la fonction texte_police
    position_texte.center = (po) #position du texte
    gameDisplay.blit(forme_texte, position_texte) #affichage du texte

def surlignage(etat):
    if etat == True :
        pig= (255,255,255)
    else :
        pig=(100, 100,100)

    return pig


while True :
    message_display("Test",(500,200),115,surlignage(False))
    pygame.display.update()