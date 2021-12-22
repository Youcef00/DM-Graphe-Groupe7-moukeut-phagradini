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
					nb_couleur +=1
					resultat[sommet] = nb_couleur
				else :
					
					for couleur in range(nb_couleur):
						if not (couleur in couleur_voisins):
							resultat[sommet] = nb_couleur	
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
		
	return resultat, frequences_couleurs
	
	
#G = nx.Graph()
#G.add_edges_from([(0, 1),
#				  (0, 2),
#				  (0, 4),
#				  (1, 2),
#				  (2, 3),
#				  (3, 4)
#		 		 ])
		 		 
#print(coloration(G, 1))
#print(coloration2(G, 1))
#print(coloration3(G, 1))
#nx.draw(G, with_labels=True, font_weight='bold')
#plt.show()
