import pygame
import random

# On lance la fenetre pygame
pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
Canvas= [1280,960]

def etoiles(taille, vitesse, nombre):
    etoile = []

    # générer tant d'étoiles et les mettre dans la liste
    for i in range(nombre):
        x = random.randrange(0, taille[0])
        y = random.randrange(0, taille[1])
        etoile.append([x, y])
        # Process each snow flake in the list
    for i in range(len(etoile)):

        # on dessine l'"étoile"
        pygame.draw.circle(screen, WHITE, etoile[i], 2)

        # Déplacer l'x de l'étoile de 1
        etoile[i][0] -= vitesse

        # Si l'étoile atteint la bordure
        if etoile[i][0] < 0 :
            # le replacer sur un y aléatoire
            y = random.randrange(0, Canvas[1])
            etoile[i][0] = Canvas[0]
            # De l'autre coté de l'écran
            x = random.randrange(0, Canvas[0])
            etoile[i][1] = y

#On définit la taille de la fenetre
screen = pygame.display.set_mode(Canvas)
pygame.display.set_caption("Fond étoilé")

#on définit une variable qui va faire appel à la synchronisation des images par pygame
clock = pygame.time.Clock()

#on initialise la boucle principale tant que l'utilisateur ne quitte pas
arret = False
while not arret:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = arret



    # fond noir
    screen.fill(BLACK)

    etoiles(Canvas,80,1100)


    # mise a jour des frames

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
