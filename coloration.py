import networkx as nx
import matplotlib.pyplot as plt


#algo gluton
#tableau de couleur avec le nombre d'apparition
# deegre, voisinage
#valeur de retour ajouter le nb de couleur ?

# parcours en largeur naif avec pour chaque sommet une couleur
#faire un algo qui tri par ordre decroissant de degre de sommets

#gerer les multis graphe ?


# nom de sommet doivent commencer a être numéroté de 0 
def coloration(g, sommet):
	nb_couleur = 0
	deja_visites = [False for s in range(g.order())]
	a_traiter = []
	a_traiter.append(sommet)
	resultat = [0 for i in range(g.order())]
	
	while a_traiter != []:
		sommet = a_traiter.pop()
		
		if not deja_visites[sommet]:
			#resultat.append(sommet)
			deja_visites[sommet] = True
			nb_couleur += 1
			resultat[sommet] = nb_couleur			
			for voisin in g.neighbors(sommet):
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
		
		# On verifie que le sommet n'est pas visité
		if not deja_visites[sommet]:
			deja_visites[sommet] = True
			
			couleur_voisins = []
			# Pour chaque voisin on va verifier : 
			# s'il est visité : on ajoute sa couleur dans la variable `couleur_voisins` (1er if)
			# s'il n'est pas visité et qu'il n'est pas dans la liste `a_traiter`, on l'ajoute (2eme if)
			for voisin in g.neighbors(sommet):
				if deja_visites[voisin]:
					couleur_voisins.append(resultat[voisin])
				if not deja_visites[voisin] and not voisin in a_traiter: 
					a_traiter.append(voisin)
			
				nb_couleur_voisins = len(couleur_voisins)
				# On verifie par la suite si le nombre de couleur disponible est égal au nombre de couleurs 
				#des voisins on ajoute une couleur et on l'attribue au sommet actuel 
				# Si non on choisi une couleur pour le sommet parmi les couleurs disponibles qui ne sont pas celles des voisins
				if nb_couleur == nb_couleur_voisins:
					nb_couleur +=1
					resultat[sommet] = nb_couleur
				else :
					for couleur in range(1, nb_couleur+1):
						if not (couleur in couleur_voisins):
							resultat[sommet] = nb_couleur
							break
	return resultat


def coloration3(g, sommet):
	nb_couleur = 0
	frequences_couleurs = []
	deja_visites = [False for s in range(g.order())]
	a_traiter = []
	a_traiter.append(sommet)
	resultat = [0 for i in range(g.order())]
	
	while a_traiter != []:
		sommet = a_traiter.pop()
		
		if not deja_visites[sommet]:
			deja_visites[sommet] = True
						
			couleur_voisins = []

			for voisin in g.neighbors(sommet):
				if deja_visites[voisin]:
					couleur_voisins.append(resultat[voisin])
				if not deja_visites[voisin] and not voisin in a_traiter:
					a_traiter.append(voisin)
			
				nb_couleur_voisins = len(couleur_voisins)

				if nb_couleur == nb_couleur_voisins:
					frequences_couleurs += [0]
					nb_couleur +=1
					
					frequences_couleurs[nb_couleur-1] += 1
					resultat[sommet] = nb_couleur
				else :
					freq_min = min(frequences_couleurs)
					min_index = frequences_couleurs.index(freq_min)
					frequences_couleurs[min_index] += 1
					resultat[sommet] = min_index
	return resultat

