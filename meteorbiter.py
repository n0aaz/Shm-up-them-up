import pygame
import random

""" On appelle nos classes définies dans des fichiers à part"""
import vaisseau
import tir

# Initialisation de pygame
pygame.init()

# Taille de l'écran , on prend un ratio de 16/9
largeur = 80*16
hauteur = 80*9
fenetre = pygame.display.set_mode([largeur, hauteur])

# Groupements/listes d'objets
liste_tir = pygame.sprite.Group()
liste_tout = pygame.sprite.Group()
liste_explosion = pygame.sprite.Group()

# Initialisation de clock pour gérer la vitesse de rafraichissement
clock = pygame.time.Clock()

arret = False

# Initialisation du vaisseau du joueur
joueur = vaisseau.Vaisseau()
liste_tout.add(joueur)
joueur.rect.x = largeur/20
joueur.rect.y = hauteur/2
heuredeces = 0

# différentes directions pour les tirs
directions = ["N", "S", "E", "O", "NE", "NO", "SE", "SO"]


# Fonction/animation explosion lors de la mort du vaisseau
def explosion(coor_x, coor_y):

    for a in range(8):
        b = tir.Explosion()
        liste_explosion.add(b)
        b.modetir = directions[a]

    for debris in liste_explosion:
        debris.rect.x = coor_x
        debris.rect.y = coor_y
        liste_tout.add(debris)
        liste_explosion.remove(debris)


###############################################Programme principal
while not arret:
    # On stoppe le programme si l'utilisateur quitte
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            arret = True

        # On tire avec le clic de la souris
        elif event.type == pygame.MOUSEBUTTONDOWN:
            balle = tir.Tir()
            # La balle est positionnée précisément sur le canon du vaisseau
            balle.rect.x = joueur.centrecanon[0]
            balle.rect.y = joueur.centrecanon[1]
            # On met toutes les "balles" dans une liste pour pouvoir par la suite
            # permettre le déplacement de tous les objets en meme temps et de vérifier
            # si il y a collision
            liste_tout.add(balle)
            liste_tir.add(balle)

        elif event.type == pygame.KEYDOWN:
            # Quand le joueur meurt on lance la méthode joueur.mort qui va lui enlever une vie
            # puis lancer l'animation d'explosion et retenir l'heure en millisecondes du décès
            joueur.mort()
            explosion(joueur.centrecanon[0], joueur.centrecanon[1])
            heuredeces = pygame.time.get_ticks()

    # Il faut laisser le joueur respirer après une mort :
    # Le vaisseau est totalement invisible pendant 2s (il a explosé)
    # Pendant 5s il réapparait en clignotant, pour indiquer au joueur qu'il doit se préparer

    temps = pygame.time.get_ticks()

    if temps - heuredeces > 2500 and temps - heuredeces < 7500 and joueur.immunite:
        joueur.cligno()
        joueur.rect.x = largeur/20
        joueur.rect.y = hauteur/2
    elif temps - heuredeces > 7500:
        joueur.immunite = False
        joueur.image.set_alpha(255)

    # On fait disparaitre les objets lorsqu'ils ne sont plus visibles , gain de mémoire
    for objet in liste_tout:
        if objet.rect.x > largeur+20:
            objet.kill()
            print('balle')
        elif objet.rect.y > hauteur+20:
            objet.kill()
            print('balle')
        elif objet.rect.x < -20:
            objet.kill()
            print('balle')
        elif objet.rect.y < -20:
            objet.kill()
            print('balle')

    # On appelle la fonction update de tous les objets en meme temps
    # pour les déplacer tous en même temps
    liste_tout.update()

    # Nettoyage de l'écran
    fenetre.fill([0, 0, 0])

    # Rendu de tous les objets
    liste_tout.draw(fenetre)

    # Affichage de tout
    pygame.display.flip()

    # Quasiment tous les écrans sont limités à 60hz de rafraichissement
    # Pourquoi vouloir aller plus vite?
    # Limite de rafraichissement à 60 fois par seconde
    clock.tick(60)

pygame.quit()
