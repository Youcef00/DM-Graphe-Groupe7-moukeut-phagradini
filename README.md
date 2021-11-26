### Binome
- Moukeut Youcef
- Phagradiani Haik

# GRAPHES-DM

## Modélisation

### Sudoku
Nous allons modéliser le problème du sudoku sous la forme d'un problème de résolution de couleurs. 
Pour modéliser notre problème sous forme d'un graphes nous allons d'abord :
	- attribuer un numéro à chaque case de la grille, une case correspond a un sommet du graphe,
	- puis relier les numeros de case d'une même **ligne**, de **colonne** et de même **sous-grilles** entre eux.
Avec ce procédé nous allons obtenir un graphe où toutes les cases serons présentes. 
Comme nous avons neuf valeurs possibles pour le sudoku nous avons besoin d'attribuer une couleur par valeur. Nous pouvons alors procéder à la résolution du graphes par l'algorithme de coloration.

Cela marche car si deux sommets reliés ne peuvent pas avoir la même couleur (=numéro) cela revient à dire qu'on attribut une couleur a un sommet et que la ligne, la collone et le sous-graphe ne peuvent pas avoir la même couleur.

Si une ou des valeurs sont présentes dans le graphe, faudra attribuer une couleur a la case (=sommet) correspondante, puis vérifie que la résolution est toujours possible, et si c'est possible nous pouvons alors commencer à applique l'algorithme de coloration. Pour verifier si la résolution est possible nous devons verifier que deux sommets du graphe de même couleur ne sont pas reliés.

### Cartes géographiques 

Pour la modélisation de la cartes géographiques, nous allons :
	- numéroter chaque pays par un numéro, un pays correspond a un sommet du graphe,
	- puis nous allons relier chaque pays limitrophe entre eux, ce qui correspond aux arêtes.
	- et ensuite procéder à la résolution du graphes à l'aide de l'algorithme de coloration.

Cela marche car les pays limitrophes ne seront pas de la même couleur car elle seront reliées et ainsi on aura une coloration correcte.

### Allocation de frequences dans les reseaux GSM

Pour la modélisation de l'allocation de frequences c'est exactement le même problème que la carte géographique. Les sommets correspondent aux antennes et on relie les sommets si les antennes sont voisines. Puis on procède à la résolution du graphe par l'algorithme de coloration.

Cela marche car les antennes voisines ne seront pas de la même fréquence car elle seront reliées et ainsi on aura une distribution de fréquence correcte.

---------------------------------------------------

En fait le problème à résoudre pour les 3 problèmes est toujours le même, cela revient à résoudre un problème de coloration. Pour résoudre les problèmes on modélise sous forme de graphe, où l'on définit les sommets et les arcs du graphe par les contraintes qu'on veut respecter, puis on procède à la résolution par l'algorithme de coloration.
