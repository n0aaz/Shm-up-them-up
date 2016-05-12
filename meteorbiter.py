import pygame
import random

""" On appelle nos classes définies dans des fichiers à part"""
from librairies import monstre, bonus, tir, vaisseau, Textes, Alicia

# On demande le nom du joueur avant l'initialisation de pygame
# Pour que l'attention du joueur soit focalisée sur le terminal
nom_joueur = input('Quel est ton nom?')

# Initialisation de pygame
pygame.init()

# Taille de l'écran , on prend un ratio de 16/9
largeur = 80*16
hauteur = 80*9

# mise en place des positions des textes
centre = [largeur / 2, hauteur / 2]
position_score = [centre[0]-160, centre[1] + 180]

# Mise en place de la fenetre Pygame
fenetre = pygame.display.set_mode([largeur, hauteur])
pygame.display.set_caption("MeteOrbitercr")

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
liste_popup = pygame.sprite.Group()

#son_gameover = pygame.mixer.Sound("ressources/son/GameOver.ogg")
#musique = pygame.mixer.Sound("ressources/son/2080-SheLikesToPlay.ogg")
police = 'ressources/polices/Minecraft.ttf'
image = pygame.image.load("ressources/image/life.png").convert()
image.set_colorkey([255,255,255])

# Initialisation de clock pour gérer la vitesse de rafraichissement
clock = pygame.time.Clock()
pygame.mouse.set_visible(True)

# Paramètres d'initialisation du jeu, etatactuel permet de choisir sur
# quel menu démarrer, quelvaisseau permet de choisir le vaisseau 1,2 ou 3
etatactuel = "Vaisseau"
quelvaisseau = 1
arret = False
score = 0
#compteur de frame(image)
compteimage = 0
initialisation = 0

###Scores###
def enreg_score(nom,score):
    #on initialise le fichier texte
    #attribut a = append, ajout au fichier

    ligne = nom + " " + str(score)
    
    with open("ressources/texte/score.txt", "a") as fichier:
        fichier.write(ligne + "\n")

def lire_score():
	# On lit le fichier texte, attribut "r" pour "read"
	with open("ressources/texte/score.txt", "r") as fichier:
		
		lignes = fichier.readlines()
		scores = []
		for ligne in lignes:
			# La fonction split() permet de découper une ligne en mots (jusqu'à ce qu'elle rencontre un espace)
			scores.append(ligne.split())
		# Les scores dans la liste sont en caractères or on veut des entiers
		for score in scores:
			score[1] = int(score[1])
		return scores

def tri_score(liste):
	
	# La fonction tridecroissant range les scores d'une liste de la forme [nom,score]
	# par ordre décroissant puis on réecrit notre liste des scores dans notre fichier
    liste_tri = Alicia.tridecroissant(liste)
    with open("ressources/texte/score.txt", "w") as fichier:
        compteur=0
        for score in liste_tri:
            compteur += 1
            #On ne garde que les 5 meilleurs scores
            if compteur <= 5:
                ligne = score[0] + " " + str(score[1])
                fichier.write(ligne + "\n")

###Scores###

###Menus### - En tant que fonction pour faciliter une utilisation ultérieure
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
    afficheurscore2.print_texte(str(entree),x+400,y)
    liste_textes.add(afficheurscore2)
    
###Menus###

def popup_score(score,x,y):
    ligne="+"+str(score)
    afficheurscore = Textes.Textes(police, 10)
    afficheurscore.print_texte(ligne,x,y)
    liste_textes.add(afficheurscore)
    return pygame.time.get_ticks()

def vaguemonstre():
        # Lotterie pour le choix de la vague
                mode = random.randrange(1, 4)
                if mode == 1:
                    #Création d'une file de 5 monstres
                    for a in range(1, 5):
                        #Appel à la classe Monstre
                        vador = monstre.Monstre()
                        #Définition du mode de déplacement
                        vador.modedeplacement = "D"
                        #Ajout dans les listes
                        liste_tout.add(vador)
                        liste_monstre.add(vador)
                        #Positionnement de départ du monstre
                        vador.rect.y = a*hauteur/5
                        vador.rect.x = largeur+10
                        #Possibilité de tirer
                        tirer(vador.rect.x, vador.rect.y, 1, False, True)
                if mode == 2:
                    for a in range(1, 5):
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

#Petite fonction utilitaire pour vider une liste d'objet
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
    # différentes directions , une explosion c'est une multitude de tirs
    # inoffensifs
    # On initialise les directions dans une liste pour pouvoir les utiliser
    # tous en meme temps
    directions = [ "NE", "NO", "SE", "SO"]
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
    #différentes directions d'un tir (joueur ou ennemi, fonction commune)
    directions = ["E", "NE", "SE"]
    #bruitage
    #son_tir = pygame.mixer.Sound("ressources/son/tir.ogg")
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

# Initialisation des meilleurs scores
meilleurs_scores = lire_score()
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

    # boucles de programme différentes selon l'etat actuel demandé par une 
    # Simple variable, permet de passer d'un écran à l'autre dans une meme
    # fenetre
    if etatactuel == "Jeu":
		
    ######################Initialisation
        if initialisation<1:
            initialisation+=1
            #chargement du vaisseau différent selon la sélection du joueur
            if quelvaisseau == 1 :
                joueur = vaisseau.Vaisseau()
            
            elif quelvaisseau == 2:
                joueur = vaisseau.Vaisseau2()
                
            elif quelvaisseau == 3:
                joueur = vaisseau.Vaisseau3()
	        
	        #Lancement de la musique
            musique.play(0,0,400)
            #Ajout du vaisseau du joueur et initialisation à un point de départ
            liste_tout.add(joueur)
            liste_joueur.add(joueur)
            joueur.rect.x = largeur/20
            joueur.rect.y = hauteur/2
            #heuredeces et delaibonus doivent etre initialisés pour permettre
            #la résurrection du joueur et la gestion des durées de bonus
            heuredeces = 0
            delaibonus = 0
            nombretir = 1
            perforant = False
    ######################Evenements
        for event in pygame.event.get():

            # On met le programme en pause si la touche échap est appuyée
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:
                    #initialisation des textes
                    init_titre("Pause", largeur/2 , 25)
                    textequitter=Textes.Textes(police,50)
                    textequitter.print_texte("Quitter",largeur/2,hauteur/2)
                    liste_textes.add(textequitter)
                    
                    #on refait appel aux fonctions de draw et display car
                    #on est maintenant dans une boucle à part tant qu'on 
                    #est sur le menu de pause
                    liste_textes.draw(fenetre)
                    pygame.display.flip()
                    while not nopause:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                nopause = True
                                vidageliste(liste_textes)
                            # On détecte la collision entre le pointeur de la souris
                            # et le texte quitter, si il y a clic et collision alors
                            # le joueur souhaite quitter, on sort de la boucle de pause
                            # et du programme principal
                            elif textequitter.rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                                nopause = True
                                arret = True

            # On tire avec le clic de la souris
            elif event.type == pygame.MOUSEBUTTONDOWN and not joueur.immunite:
                if quelvaisseau == 1 or quelvaisseau == 3:
                    tirer(joueur.centrecanon[0], joueur.centrecanon[1], nombretir, perforant, False)
                elif quelvaisseau == 2:
                    tirer(joueur.centrecanon[0], joueur.centrecanon[1], nombretir, perforant, False)
                    tirer(joueur.centrecanon2[0], joueur.centrecanon2[1], nombretir, perforant, False)
        liste_detruits.add(liste_tir, liste_monstre, liste_bonus)

    ###Collisions

        # Collision entre le joueur et : Ennemis, tirs ennemis, bonus
        for adetruire in liste_detruits:
			#spritecollide vérifie simplement si les coordonnées d'un objet adetruire
			#quelconque ne sont pas les mêmes qu'un objet de la liste_joueur (soit le vaisseau)
			#puis si c'est le cas, ces objets sont placés dans liste_collision_detruits
            liste_collision_detruits = pygame.sprite.spritecollide(adetruire, liste_joueur, False)
            
            #lorsqu'un objet est dans cette liste, c'est qu'une collision a eu lieu entre le joueur
            #et un objet destructible (tir, ennemi, bonus)
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
                    if not joueur.immunite: #bonus inopérants si le joueur vient de mourir
                        # on demande l'heure en ms et on l'enregistre: c'est le moment ou
                        # le bonus est activé, cette variable permettra de la désactiver
                        # au bout d'une durée déterminée plus tard
                        delaibonus = pygame.time.get_ticks()
                        if adetruire.plus:
                            nombretir = 3
                        elif adetruire.rond:
                            perforant = True
                        # Le bonus explose, est actif, le vaisseau n'est pas détruit
                        # Sinon à quoi bon chercher les bonus?
                        explosion(adetruire.rect.x, adetruire.rect.y)
                        adetruire.kill()

        #Collisions entre une balle alliée et un ennemi
        for touche in liste_tir:
            if not touche.ennemi:
                # Spritecollide nous permet de prendre un objet d'un groupe
                # si il est en collision avec le ou les objets mentionnés
                liste_collision_monstre = pygame.sprite.spritecollide(touche, liste_monstre, False)
                for objet in liste_collision_monstre:
                        explosion(objet.rect.x, objet.rect.y)
                        objet.kill()
                        #la "balle" tirée est detruite uniquement si elle 
                        #n'est pas perforante, auquel cas elle continue sa course
                        if not perforant:
                            touche.kill()
                        score += 100
                        print(score)#"""debug"""

    #####################Evenements

        # Horloge rafraichie à chaque image
        temps = pygame.time.get_ticks()
        # on lance une vague de monstres toutes les 5000ms
        if temps%5000<=50:
            vaguemonstre()
    ### Gestion de bonus aléatoire

        # Une chance sur 1000 à chaque image de faire naitre un bonus
        loterie = random.randrange(0, 1000)

        # Le bonus apparait aléatoirement en haut de l'écran si la loterie
        # aléatoire est égale à un nombre choisi, peu importe lequel entre
        # 0 et 1000
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
            score += 1000

            

    ###Resurrection du joueur

        # Il faut laisser le joueur respirer après une mort :
        # Le vaisseau est totalement invisible pendant 2s (il a explosé)
        # Pendant 5s il réapparait en clignotant, pour indiquer au joueur qu'il doit se préparer

        if temps - heuredeces >= 2500 and temps - heuredeces < 7500 and joueur.immunite:
            if temps - heuredeces < 2600 and joueur.vie > 0:
                az=1
				#bruitage, réapparition tant qu'il reste des vies
                #bruit_reapparition = pygame.mixer.Sound("ressources/son/reapparition.ogg")
               # bruit_reapparition.play()

            # pas de résurrection si le joueur n'a plus de vie
            # Destruction de tous les objets et lancement menu gameover
            if joueur.vie == 0:
                print("Game Over")
                #musique.stop()
                #son_gameover.play(0,0,400)
                vidageliste(liste_tout)
                initialisation = 0
                etatactuel = "GameOver"
            
            #Le joueur clignote, son déplacement n'est plus possible que sur un axe vertical
            #le temps de sa réappariton

            joueur.cligno()
            joueur.rect.x = largeur/20
            joueur.rect.y = pygame.mouse.get_pos()[1]
            #On force la position de la souris là ou est le vaisseau , anti triche
            pygame.mouse.set_pos([joueur.rect.x, joueur.rect.y])
        
        #Le joueur n'est plus immune au bout de 7.5s et ne clignote plus
        elif temps - heuredeces > 7500:
            joueur.immunite = False
            joueur.image.set_alpha(255)

    elif etatactuel == "Score":
        if initialisation <1 :
            initialisation += 1
            # Reinitialisation des meilleurs scores, au cas ou un record ait été battu précédemment
            meilleurs_scores = lire_score()
            # Tri de l'ordre des scores du fichier texte
            tri_score(meilleurs_scores)
            meilleurs_scores = lire_score()
            
            init_titre("Meilleurs scores", largeur/2 - 200, 25)
            boutonmenu = Textes.Textes(police, 50)
            boutonmenu.print_texte(" <= Menu ",0,hauteur-50)
            liste_textes.add(boutonmenu)
            
            # pour chaque score dans le fichier texte on initialise une
            # ligne affichée du type numéro - nom : score
            for a in range (1,len(meilleurs_scores)+1):
                b= str(a)+" - "+meilleurs_scores[a-1][0]+":"
                init_score(meilleurs_scores[a-1][1],b,350,a*(hauteur/6))
        
        # utilisation d'un texte en guise de bouton , voir plus haut le menu pause
        for event in pygame.event.get():
            if boutonmenu.rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONUP:
                arret = True
        
    elif etatactuel == "GameOver":

        compteimage += 1

		#on n'initialise les textes qu'une seule fois pour éviter
		#de générer des milliers d'objets
        if initialisation <1:
		    #on enregistre le score dans le fichier uniquement si celui ci
            #est meilleur que le dernier meilleur score et que le fichier
            #ne contient pas plus de 5 scores
            if int(score) > int(meilleurs_scores[-1][1]):
                enreg_score(nom_joueur,score)
                print(score,meilleurs_scores[-1][1])
            initialisation +=1
            init_titre("Game Over", centre[0]-180, centre[1])
            init_score(score,"score:",position_score[0],position_score[1])

        for texte in liste_textes:
        # faire défiler le score et le gameover au bout de 10s (60frames affichés par s)
            if compteimage >= 60*10:
                texte.rect.y -= 2
        
        # Passage à l'écran des scores lorsque le défilement est terminé:
        # Au dela de certaines coordonnées, tout objet sortant de l'écran
        # Est détruit d'ou la longueur de la liste de texte qui est nulle
        if len(liste_textes) == 0:
            etatactuel = "Score"
            initialisation = 0

    elif etatactuel == "Vaisseau":
		
		#initialisation de la mise en page, des éléments
        if initialisation<1:
            initialisation+=1
			
            init_titre("Vaisseaux",largeur/2-100,hauteur/10)
            init_score("","choisissez votre vaisseau mon colonel",largeur/2-400,2*hauteur/10)    
            
            #on initialise les vaisseaux de démonstration
            v1=vaisseau.Vaisseau()
            v1.demo = True
            v2=vaisseau.Vaisseau2()
            v2.demo = True
            v3=vaisseau.Vaisseau3()
            v3.demo = True
            
            liste_joueur.add(v1,v2,v3)
            liste_tout.add(liste_joueur)
            
            #On initialise leurs positions, fixes
            v1.rect.x = (largeur/8)
            v1.rect.y = hauteur/2
            v2.rect.x = 3*(largeur/8)
            v2.rect.y = hauteur/2
            v3.rect.x = 5*(largeur/8)
            v3.rect.y = hauteur/2
            
            init_score("","STX-645",v1.rect.x,v1.rect.y + v1.taille[1] + 25)
            init_score("","Lamernoir",v2.rect.x,v2.rect.y + v2.taille[1] + 25)
            init_score("","Minipoulpe",v3.rect.x,v3.rect.y + v3.taille[1] + 25)
            
            boutonmenu = Textes.Textes(police, 50)
            boutonmenu.print_texte(" <= Menu ",0,hauteur-50)
            liste_textes.add(boutonmenu)
    
        #Sélections à la souris du vaisseau
        if v1.rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
            quelvaisseau = 1
            v1.choix=True
            v2.choix=False
            v3.choix=False
            
        elif v2.rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
            quelvaisseau = 2
            v1.choix=False
            v2.choix=True
            v3.choix=False

        elif v3.rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
            quelvaisseau = 3
            v1.choix=False
            v2.choix=False
            v3.choix=True
        
        #Bouton menu comme dans le menu des scores pour retourner au menu (quitte
        #le jeu pour l'instant car le menu n'est pas terminé)
        if boutonmenu.rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONUP:
                initialisation=0
                vidageliste(liste_joueur)
                vidageliste(liste_textes)
                etatactuel="Jeu"

    elif etatactuel == "menuprincipal" :
    # initialisation de la mise en page, des éléments
        if initialisation < 1:
            initialisation += 1

        init_titre("Vaisseaux", largeur / 2 - 100, hauteur / 10)


    # Option commune, peu importe le menu, si le joueur quitte, le jeu s'arrete
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
    
    ###Alicia
    try:
        if etatactuel == "Jeu" :
            Alicia.afficheur_vies(fenetre,hauteur,joueur,image)
            Alicia.afficheur_scores(fenetre,score,police)
    except NameError:
        pass
    
    # Rendu de tous les objets
    liste_tout.draw(fenetre)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
