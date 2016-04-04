import pygame
import random

""" On appelle nos classes définies dans des fichiers à part"""
from librairies import monstre, bonus, tir, vaisseau, Textes

# Initialisation de pygame
pygame.init()

# Taille de l'écran , on prend un ratio de 16/9
largeur = 62*16
hauteur = 62*9

# mise en place des positions des textes
centre = [largeur / 2, hauteur / 2]
position_score = [centre[0]-160, centre[1] + 180]

fenetre = pygame.display.set_mode([largeur, hauteur])
pygame.display.set_caption("MeteOrbiter (nom temporaire)")

# Groupements/listes d'objets
liste_tir = pygame.sprite.Group()
liste_tout = pygame.sprite.Group()
liste_explosion = pygame.sprite.Group()
liste_fond = pygame.sprite.Group()
liste_bonus = pygame.sprite.Group()
liste_joueur = pygame.sprite.Group()
liste_monstre = pygame.sprite.Group()
liste_detruits = pygame.sprite.Group()
liste_textes = pygame.sprite.Group()

son_gameover = pygame.mixer.Sound("ressources/son/GameOver.ogg")
musique = pygame.mixer.Sound("ressources/son/2080-SheLikesToPlay.ogg")
police = 'ressources/polices/Minecraft.ttf'

# Initialisation de clock pour gérer la vitesse de rafraichissement
clock = pygame.time.Clock()
pygame.mouse.set_visible(True)

etatactuel = "Jeu"
quelvaisseau = 3
arret = False
score = 0
#compteur de frame(image)
compteimage = 0
initialisation = 0

# Initialisation du vaisseau du joueur
if etatactuel == "Jeu":
	
    #chargement du vaisseau selon la sélection du joueur
    if quelvaisseau == 1 :
        joueur = vaisseau.Vaisseau()

    elif quelvaisseau == 2:
        joueur = vaisseau.Vaisseau2()
        
    elif quelvaisseau == 3:
        joueur = vaisseau.Vaisseau3()
	
    musique.play(0,0,400)
    liste_tout.add(joueur)
    liste_joueur.add(joueur)
    joueur.rect.x = largeur/20
    joueur.rect.y = hauteur/2
    heuredeces = 0
    delaibonus = 0
    nombretir = 1
    perforant = False

###Menus###
def init_titre(entree,x,y):
    #Initialisation du texte (police, taille) puis affichage dans les positions données
    titre = Textes.Textes(police, 50)
    titre.print_texte(entree,x,y)
    liste_textes.add(titre)

def init_score(entree,entree2,x,y):
    afficheurscore = Textes.Textes(police, 35)
    afficheurscore.print_texte(entree2,x,y)
    liste_textes.add(afficheurscore)
    
    afficheurscore2 = Textes.Textes(police, 35)
    afficheurscore2.print_texte(str(entree),x+200,y)
    liste_textes.add(afficheurscore2)

    
###Menus###

def vaguemonstre():
                mode = random.randrange(1, 4)
                if mode == 1:
                    for a in range(1, 5):
                        vador = monstre.Monstre()
                        vador.modedeplacement = "D"
                        liste_tout.add(vador)
                        liste_monstre.add(vador)
                        vador.rect.y = a*hauteur/5
                        vador.rect.x = largeur+10
                        tirer(vador.rect.x, vador.rect.y, 1, False, True)
                if mode == 2:
                    for a in range(1, 10):
                        vador = monstre.Monstre()
                        vador.modedeplacement = "D"
                        liste_tout.add(vador)
                        liste_monstre.add(vador)
                        vador.rect.y = a*hauteur/10
                        vador.rect.x = largeur+10
                if mode == 3:
                    vador = monstre.Monstre()
                    vador.modedeplacement = "S"
                    liste_tout.add(vador)
                    liste_monstre.add(vador)
                    vador.naissance = hauteur/2

def vidageliste(liste):
	for a in liste:
		a.kill()

def surlignage():
    for texte in liste_textes:
        # surligner le score lorsque le curseur passe dessus:
        if texte.rect.collidepoint(pygame.mouse.get_pos()):
            texte.surligne = True
        else:
            texte.surligne = False

# Fonction/animation explosion lors de la mort du vaisseau


def explosion(coor_x, coor_y):
    # différentes directions pour les tirs
    directions = ["N", "S", "E", "O", "NE", "NO", "SE", "SO"]
    for petitcompteur in range(len(directions)):
        b = tir.Explosion()
        liste_explosion.add(b)
        b.modetir = directions[petitcompteur]

    for debris in liste_explosion:
        debris.rect.x = coor_x
        debris.rect.y = coor_y
        liste_tout.add(debris)
        liste_explosion.remove(debris)

# Fonction tirer avec les coordonnées du point de départ, le nombre de tirs
# la direction du tir, et l'attribut perforant activé par un bonus


def tirer(coor_x, coor_y, nbtir, balles_perforantes, ennemi):
    directions = ["E", "NE", "SE"]
    son_tir = pygame.mixer.Sound("ressources/son/tir.ogg")
    son_tir.play()
    for numerodirection in range(nbtir):
            if ennemi:
                balle = tir.Tirennemi()
            else:
                balle = tir.Tir()
                balle.modetir = directions[numerodirection]
            liste_tir.add(balle)
            if balles_perforantes:
                balle.perforant = True
            # La balle est positionnée précisément sur le canon du vaisseau
            balle.rect.x = coor_x
            balle.rect.y = coor_y
            # On met toutes les "balles" dans une liste pour pouvoir par la suite
            # permettre le déplacement de tous les objets en meme temps et de vérifier
            # si il y a collision
            liste_tout.add(balle)

# Génération aléatoire d'étoiles avant le démarrage du jeu
for et in range(250):
    etoile = tir.Etoiles()
    etoile.rect.x = random.randrange(0, largeur)
    etoile.rect.y = random.randrange(0, hauteur)
    liste_fond.add(etoile)
    liste_tout.add(etoile)

###############################################Programme principal######################################################

while not arret:
    # On stoppe le programme si l'utilisateur quitte
    nopause = False
    surlignage()		
    #if etatactuel == "Menu":
    #Travaux en cours#

    if etatactuel == "Jeu":
    ######################Evenements
        for event in pygame.event.get():

            # On met le programme en pause si la touche espace est appuyée
            if event.type == pygame.KEYDOWN :#and event.key == pygame.K_ESCAPE:
                    
                    init_titre("Pause", largeur/2 - 200, 25)
                    textequitter=Textes.Textes(police,50)
                    textequitter.print_texte("Quitter",centre[0],centre[1]+50)
                    liste_textes.add(textequitter)
                    
                    liste_textes.draw(fenetre)
                    pygame.display.flip()
                    while not nopause:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                nopause = True
                                vidageliste(liste_textes)
                            #
                            elif textequitter.rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                                nopause = True
                                arret = True

            # On tire avec le clic de la souris
            elif event.type == pygame.MOUSEBUTTONDOWN and not joueur.immunite:
                tirer(joueur.centrecanon[0], joueur.centrecanon[1], nombretir, perforant, False)


        liste_detruits.add(liste_tir, liste_monstre, liste_bonus)

    ###Collisions

        # Collision entre le joueur et : Ennemis, tirs ennemis, bonus
        for adetruire in liste_detruits:
            liste_collision_detruits = pygame.sprite.spritecollide(adetruire, liste_joueur, False)
            for detruit in liste_collision_detruits:
                if adetruire.ennemi:
                    if not joueur.immunite:
                        adetruire.kill()
                        # Quand le joueur meurt on lance la méthode joueur.mort qui va lui enlever une vie
                        # puis lancer l'animation d'explosion et retenir l'heure en millisecondes du décès
                        joueur.mort()
                        explosion(joueur.centrecanon[0], joueur.centrecanon[1])
                        heuredeces = pygame.time.get_ticks()
                elif adetruire.bonus:
                    if not joueur.immunite:
                        delaibonus = pygame.time.get_ticks()
                        if adetruire.plus:
                            nombretir = 3
                        elif adetruire.rond:
                            perforant = True
                        explosion(adetruire.rect.x, adetruire.rect.y) #Test d'explosiooon
                        adetruire.kill()

        #Collisions entre une balle alliée et un ennemi
        for touche in liste_tir:
            if not touche.ennemi:
                # Spritecollide nous permet de prendre un objet d'un groupe
                # si il est en collision avec le ou les objets mentionnés
                liste_collision_monstre = pygame.sprite.spritecollide(touche, liste_monstre, False)
                for objet in liste_collision_monstre:
                        explosion(objet.rect.x, objet.rect.y) #explosion
                        objet.kill()
                        if not perforant:
                            touche.kill()
                        score += 100
                        print(score)

    #####################Evenements

        # Horloge rafraichie à chaque image
        temps = pygame.time.get_ticks()
        if temps%5000<=50:
            vaguemonstre()
    ### Gestion de bonus aléatoire

        # Une chance sur 1000 à chaque image de faire naitre un bonus
        loterie = random.randrange(0, 1000)

        # Le bonus apparait aléatoirement en haut de l'écran
        if loterie == 3:
            #Tirage au sort pour savoir quel bonus va sortir
            quelbonus = random.randrange(1, 3)
            if quelbonus == 1:
                bon = bonus.Bonusplus()
                bon.naissance = random.randrange(0, largeur)
                liste_tout.add(bon)
                liste_bonus.add(bon)
            elif quelbonus == 2:
                bon = bonus.Bonusrond()
                bon.naissance = random.randrange(0, largeur)
                liste_tout.add(bon)
                liste_bonus.add(bon)

        # Les bonus sont actifs pendant 15s (soit 15000ms), au dela, tout retourne dans l'ordre
        if temps - delaibonus > 15000:
            nombretir = 1
            perforant = False
        
        # Offrir une vie au joueur tous les 10000 points (c'est déjà assez dur comme ça)
        if score % 10000 == 0 and score > 0:
            joueur.vie += 1
            

    ###Resurrection du joueur

        # Il faut laisser le joueur respirer après une mort :
        # Le vaisseau est totalement invisible pendant 2s (il a explosé)
        # Pendant 5s il réapparait en clignotant, pour indiquer au joueur qu'il doit se préparer

        if temps - heuredeces >= 2500 and temps - heuredeces < 7500 and joueur.immunite:
            if temps - heuredeces < 2600 and joueur.vie > 0:
                bruit_reapparition = pygame.mixer.Sound("ressources/son/reapparition.ogg")
                bruit_reapparition.play()

            # pas de résurrection si le joueur n'a plus de vie
            # Destruction de tous les objets et lancement menu gameover
            if joueur.vie == 0:
                print("Game Over")
                son_gameover.play(0,0,400)
                vidageliste(liste_tout)
                etatactuel = "GameOver"

            joueur.cligno()
            joueur.rect.x = largeur/20
            joueur.rect.y = pygame.mouse.get_pos()[1]
            pygame.mouse.set_pos([joueur.rect.x, joueur.rect.y])
        elif temps - heuredeces > 7500:
            joueur.immunite = False
            joueur.image.set_alpha(255)


    elif etatactuel == "Score":
        if initialisation <1 :
            initialisation += 1
            init_titre("Meilleurs scores", largeur/2 - 200, 25)
            boutonmenu = Textes.Textes(police, 50)
            boutonmenu.print_texte(" <= Menu ",0,hauteur-50)
            liste_textes.add(boutonmenu)
            for a in range (1,6):
                b= str(a)+"-"
                init_score(score,b,350,a*(hauteur/6))
        
        for event in pygame.event.get():
            if boutonmenu.rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONUP:
                arret = True
        

    elif etatactuel == "GameOver":

        compteimage += 1

		#on n'initialise les textes qu'une seule fois pour éviter
		#de générer des milliers d'objets
        if initialisation <1:
            initialisation +=1
            init_titre("Game Over", centre[0]-180, centre[1])
            init_score(score,"score:",position_score[0],position_score[1])

        for texte in liste_textes:
        # faire défiler le score et le gameover au bout de 10s (60frames affichés par s)
            if compteimage >= 60*10:
                texte.rect.y -= 2
                    
        if len(liste_textes) == 0:
            etatactuel = "Score"
            initialisation = 0
            #nomjoueur = Textes.Textes(police,50)
            #nomjoueur.print_texte("Quel est ton nom?", centre[0]-nomjoueur.centre, hauteur/6)
            #liste_textes.add(nomjoueur)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            arret = True
            
    ###Destruction/recyclage des objets inutiles


    # On fait disparaitre les objets lorsqu'ils ne sont plus visibles , gain de mémoire
    for objet in liste_tout:
        if objet.rect.x > largeur + 20:
            objet.kill()
        elif objet.rect.y > hauteur + 20:
            objet.kill()
        elif objet.rect.x < -20:
            # Les étoiles ne disparaissent pas, elles reviennent de l'autre côté: recyclage
            if objet.etoile:
                objet.rect.y = random.randrange(0, hauteur)
                objet.rect.x = largeur + 20
            else:
                objet.kill()
        elif objet.rect.y < -20:
            objet.kill()

    liste_tout.add(liste_textes)
    # On appelle la fonction update de tous les objets en meme temps
    # pour les déplacer tous en même temps
    liste_tout.update()

    # Nettoyage de l'écran
    fenetre.fill([0, 0, 0])

    # Rendu de tous les objets
    liste_tout.draw(fenetre)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
