import pygame


pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
gameDisplay = pygame.display.set_mode((display_width,display_height))

def texte_police(texte, police):
    forme_texte = police.render(texte, True, white)
    return forme_texte, forme_texte.get_rect()


def message_display(text):
    taille_texte = pygame.font.Font('ressources/polices/minecraft.ttf',115)
    forme_texte, position_texte = texte_police(text, taille_texte)
    position_texte.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(forme_texte, position_texte)


while True :
    message_display("Test")
    pygame.display.update()

