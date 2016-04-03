import pygame


class Vaisseau(pygame.sprite.Sprite):
    """ On crée une classe vaisseau , cette classe herite des caractéristiques de la librairie Sprite de Pygame qui va
     Servir a faire une image fixe et mobile du vaisseau"""

    def __init__(self):
        """ Le constructeur de la classe """

        # On appelle le constructeur de la classe parent de notre classe, c'est à dire la classe Sprite de Pygame
        super().__init__()

        # Chargement de l'image du vaisseau ; ne pas oublier convert qui va rendre le fichier manipulable
        # Ne pas oublier de rendre le fond blanc du vaisseau transparent
        self.image = pygame.image.load("ressources/image/vaisseau.png").convert()
        self.image.set_colorkey([255, 255, 255])

        # Taille de l'image du vaisseau, pour faciliter les calculs
        self.taille = self.image.get_size()

        # Appel des coordonnées (taille) de l'image pour en faire les coordonnées du vaisseau
        self.rect = self.image.get_rect()

        # On définit des coordonnées du centre du canon pour faciliter le placement ultérieur
        self.centrecanon = [self.rect.x + self.taille[0] / 2 + 15, self.rect.y + self.taille[1] / 2 - 1]

        # On a trois vies
        self.vie = 3

        # Cette petite variable nous permettra par la suite d'ignorer les collisions quand il est activé
        self.immunite = False

        self.apparition = True
        
    """ Methode (fonction) de la classe pour le mouvement du vaisseau qui suivra celui de la souris"""

    def update(self):
        # On demande la position de la souris et on la
        # stocke dans une liste de deux valeurs x et y
        position = pygame.mouse.get_pos()

        # Actualisation de la position calculée du centre du canon
        self.centrecanon = [self.rect.x + self.taille[0] / 2 + 15, self.rect.y + self.taille[1] / 2 - 1]

        # La position du vaisseau sera donc celle de la souris
        if not self.immunite:
            self.rect.x = position[0]
            self.rect.y = position[1]

    def mort(self):

        # Lorsque la mort est demandée , on pert une vie mais on devient immunisé pour éviter d'en perdre plusieurs
        self.vie -= 1
        self.immunite = True
        self.image.set_alpha(0)

        # Et est joué le bruit d'explosion
        explosion = pygame.mixer.Sound("ressources/son/explosion.ogg")
        explosion.play()

    def cligno(self):

        # On fait clignoter l'image du vaisseau en faisant varier la transparence de ce dernier
        opacité = self.image.get_alpha()
        if self.apparition:
            opacité += 4
            if opacité > 255:
                self.apparition = False
        else:
            opacité -= 4
            if opacité < 10:
                self.apparition = True
        self.image.set_alpha(opacité)
        
class Vaisseau2(Vaisseau):
	def __init__(self):
		
		#le vaisseau 2 est comme le vaisseau 1 mais avec une image différente
		super().__init__()

		self.image = pygame.image.load("ressources/image/vaisseau2f1.png").convert()
		self.image.set_colorkey([255, 255, 255])
		
		#Taille de l'image du vaisseau, pour faciliter les calculs
		self.taille = self.image.get_size()

        # Appel des coordonnées (taille) de l'image pour en faire les coordonnées du vaisseau
		self.rect = self.image.get_rect()

        # On définit des coordonnées du centre du canon pour faciliter le placement ultérieur
		self.centrecanon = [self.rect.x + self.taille[0] / 2 + 30, self.rect.y + self.taille[1] / 2 - 1]
        
		#compteur c qui va nous permettre d'incrémenter l'index de liens
		self.c = 0
        #compteur d pour compter les images seules
		self.d = 0 
        #liens des différentes images de l'animation du vaisseau
		self.lienframe = ["ressources/image/vaisseau2f1.png","ressources/image/vaisseau2f2.png","ressources/image/vaisseau2f3.png"]
		
	def update(self):
		#on réutilise le update défini pour notre premier vaisseau
		super().update()

		#conditions if > plutot que modulo pour éviter que les variables
		#prennent des valeurs trop grandes et surchargent la mémoire

		#d est utilisé pour n'incrémenter c que toutes les 6 frames
		if self.d >6 : 
			self.c += 1
			self.d = 0
			
		if self.c > 2 :
			self.c = 0
			
		if not self.immunite:
		    self.image = pygame.image.load(self.lienframe[self.c]).convert()
		    self.image.set_colorkey([255, 255, 255])
		self.d += 1
		
class Vaisseau3(Vaisseau2):
	def __init__(self):
		
		#le vaisseau 2 est comme le vaisseau 1 mais avec une image différente
		super().__init__()

		self.image = pygame.image.load("ressources/image/vaisseau3f1.png").convert()
		self.image.set_colorkey([255, 255, 255])
		
		#Taille de l'image du vaisseau, pour faciliter les calculs
		self.taille = self.image.get_size()

        # Appel des coordonnées (taille) de l'image pour en faire les coordonnées du vaisseau
		self.rect = self.image.get_rect()

        # On définit des coordonnées du centre du canon pour faciliter le placement ultérieur
		self.centrecanon = [self.rect.x + self.taille[0] / 2 + 30, self.rect.y + self.taille[1] / 2 - 1]

		self.lienframe = ["ressources/image/vaisseau3f1.png","ressources/image/vaisseau3f2.png","ressources/image/vaisseau3f3.png"]

	

