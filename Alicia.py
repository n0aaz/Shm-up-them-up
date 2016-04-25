def minimum (x) :
    lg  = len(x)
    min = x[0]
    for i in range (lg):
        if x[i][1]<min[1] :
            min = x[i]
    return (min)

def tricroissant(x):
    tri = []
    lg  = len(x)
    for i in range (lg) :
        tri.append(minimum(x))
        print (tri)
        min = minimum(x)
        x.remove (min)
    return tri
    
def tridecroissant(x):
	y = tricroissant(x)
	tri = []
	lg = len(y)
	for i in range(-1,-lg-1,-1):
		tri.append(y[i])
		print (tri)
	return tri

def afficheur_vies(fenetre,joueur):
    hauteur=60*9
    image = pygame.image.load("ressources/image/vie.png").convert()
    image.set_colorkey([255,255,255])
    for a in range (0,joueur.vie):
        fenetre.blit(image,[50*a,hauteur-100])
        
        
def afficheur_scores(fenetre,score,police):
    compteurscore = Textes.Textes(police, 35)
    compteurscore.print_texte("score:"+str(score),50,50)
    fenetre.blit(compteurscore.image,[50,50])
