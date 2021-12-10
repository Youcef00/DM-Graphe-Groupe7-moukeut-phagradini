### Binome
- Moukeut Youcef
- Phagradiani Haik

# GRAPHES-DM

## Rendu 1

### Modélisation

#### Sudoku
Nous allons modéliser le problème du sudoku sous la forme d'un problème de résolution de couleurs. 
Pour modéliser notre problème sous forme d'un graphe, nous allons d'abord :
	- attribuer un numéro à chaque case de la grille, une case correspond à un sommet du graphe,
	- puis relier les numéros de case d'une même **ligne**, de **colonne** et de même **sous-grilles** entre eux.
Avec ce procédé, nous allons obtenir un graphe où toutes les cases seront présentes. 
Comme nous avons neuf valeurs possibles pour le sudoku, nous avons besoin d'attribuer une couleur par valeur. Nous pouvons alors procéder à la résolution du graphe par l'algorithme de coloration.

Cela marche, car si deux sommets reliés ne peuvent pas avoir la même couleur (= numéro) cela revient à dire qu'on attribut une couleur a un sommet et que la ligne, la colonne et le sous-graphe ne peuvent pas avoir la même couleur.

Si une ou des valeurs sont présentes dans le graphe, faudra attribuer une couleur à la case (= sommet) correspondante, puis vérifie que la résolution est toujours possible, et si c'est possible nous pouvons alors commencer à applique l'algorithme de coloration. Pour vérifier si la résolution est possible nous devons vérifier que deux sommets du graphe de même couleur ne sont pas reliés.

#### Cartes géographiques 

Pour la modélisation de la carte géographique, nous allons :
	- numéroter chaque pays par un numéro, un pays correspond à un sommet du graphe,
	- puis nous allons relier chaque pays limitrophe entre eux, ce qui correspond aux arêtes.
	- et ensuite procéder à la résolution du graphe à l'aide de l'algorithme de coloration.

Cela marche, car les pays limitrophes ne seront pas de la même couleur, elles seront reliées, ainsi, on aura une coloration correcte.

#### Allocation de fréquences dans les réseaux GSM

Pour la modélisation de l'allocation de fréquence, c'est exactement le même problème que la carte géographique. Les sommets correspondent aux antennes et on relie les sommets si les antennes sont voisines. Puis on procède à la résolution du graphe par l'algorithme de coloration.

Cela marche, car les antennes voisines ne seront pas de la même fréquence, elles seront reliées, ainsi, on aura une distribution de fréquence correcte.

---------------------------------------------------

En fait, le problème à résoudre pour les 3 problèmes est toujours le même, cela revient à résoudre un problème de coloration. Pour résoudre les problèmes, on modélise sous forme de graphe, où l'on définit les sommets et les arcs du graphe par les contraintes qu'on veut respecter, puis on procède à la résolution par l'algorithme de coloration. L'algorithme de coloration attribut une couleur a chaque sommet et faisant attention à ne pas attribuer une même couleur au sommet adjacent.


## Rendu 2


- Un "problème difficile" est un problème avec une complexité importante, comme les problèmes N=NP
- Une heuristique est une solution qui se rapproche d'une solution la plus optimale.

- Pour l'algorithme naïf nous avons décider de parcourir le graphe en largeur et associer une couleur différente à chaque sommet
- Pour l'algorithme glouton nous avons conservé le parcours en largeur du graphe mais avant d'associer une couleur à chaque sommet, nous regarder d'abord les couleurs des voisins, puis associons une couleur qui n'est pas celle des voisins parmis les couleurs déjà utilisées, s'il n'y a pas de couleurs non utilisée on ajoute donc une coleur.
- Pour l'algorithme avancé nous conservons le parcours en largeur mais maintenant nous stoquons la fréquence des couleurs déjà utilisés, sauf que après avoir regardé la couleur des voisins (comme dans l'algorithme glouton), nous associons au sommet la couleur la moins fréquente, et s'il n'y a pas assez de couleurs on ajoute alors une couleur supplémentaire (comme précédament). 

Voici le code des deux premiers algorithmes : 

```py
# Algo naif
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
			resultat[sommet] = nb_couleur			
			for voisin in graphe.neighbors(sommet):
				if not deja_visites[voisin] and not voisin in a_traiter:
					a_traiter.append(voisin)
	return resultat
```
```py
# Algo glouton
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
						
			couleur_voisins = []

			for voisin in graphe.neighbors(sommet):
				if deja_visites[voisin]:
					couleur_voisins.append(resultat[voisin])
				if not deja_visites[voisin] and not voisin in a_traiter:
					a_traiter.append(voisin)
			
				nb_couleur_voisins = len(couleur_voisins)

				if nb_couleur == nb_couleur_voisins:
					nb_couleur +=1
					resultat[sommetsss] = nb_couleur
				else :
					for couleur in range(nb_couleur):
						if not (couleur in couleur_voisins):
							resultat[sommet] = nb_couleur
							
	return resultat
```

```py
# Algo avance
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
			resultat.append(sommet)
			deja_visites[sommet] = True
						
			couleur_voisins = []

			for voisin in graphe.neighbors(sommet):
				if deja_visites[voisin]:
					couleur_voisins.append(resultat[voisin])
				if not deja_visites[voisin] and not voisin in a_traiter:
					a_traiter.append(voisin)
			
				nb_couleur_voisins = len(couleur_voisins)

				if nb_couleur == nb_couleur_voisins:
					nb_couleur +=1
					frequences_couleurs[nb_couleur-1] = 1
					resultat[sommet] = nb_couleur
				else :
					freq_min = min(frequences_couleurs)
					min_index = frequences_couleurs.index(freq_min)
					frequences_couleurs[min_index] += 1
					resultat[sommet] = min_index
		
	return resultat
```




