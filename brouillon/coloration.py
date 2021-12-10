
#algo gluton
#tableau de couleur avec le nombre d'apparition
# deegre, voisinage

# parcours en largeur naif avec pour chaque sommet une couleur

def coloration(g, sommet):
	nb_couleur = 0
	deja_visites = [False for s in range(g.order())]
	a_traiter = []
	a_traiter.append(sommet)
	resultat = [0 for i in range(g.order())]
	
	while a_traiter != []:
		sommet = a_traiter.pop()
		
		if not deja_visites[sommet]:
			resultat.append(sommet)
			deja_visites[sommet] = True
			nb_couleur += 1
			resultat = nb_couleur			
			for voisin in graphe.neighbors(sommet):
				if not deja_visites[voisin] and not voisin in a_traiter:
					a_traiter.append(voisin)
	return resultat
	
#algo glouton
def coloration2(g, sommet):
	nb_couleur = 0
	deja_visites = [False for s in range(g.order())]
	a_traiter = []
	a_traiter.append(sommet)
	resultat = [0 for i in range(g.order())]
	
	while a_traiter != []:
		sommet = a_traiter.pop()
		
		if not deja_visites[sommet]:
			resultat.append(sommet)
			deja_visites[sommet] = True
			nb_couleur += 1
			resultat = nb_couleur
			
			couleur_voisins = []		
			for voisin in graphe.neighbors(sommet):
				if deja_visites[voisin]:
					couleur_voisins.append(resultat[voisin])
				if not deja_visites[voisin] and not voisin in a_traiter:
					a_traiter.append(voisin)
			
				nb_couleur_voisins = len(couleur_voisins)
				if nb_couleur == nb_couleur_voisins:
					nb_couleur +=1
					resultat[voisin] = nb_couleur
				else :
					for couleur in range(nb_couleur):
						if not (couleur in couleur_voisins):
							resultat[voisin] = nb_couleur
							
	return resultat
	



