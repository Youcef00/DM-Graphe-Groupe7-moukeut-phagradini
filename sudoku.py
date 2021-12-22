import sys
import networkx as nx
import matplotlib.pyplot as plt

from coloration import *

def voisins(fichier):
	liste_voisins = []
	
	with open(fichier) as fp:
		for line in fp:
			if line != "\n":
				rendu = line.split()
				liste_voisins.append(tuple(rendu))
	fp.close()
	
	return liste_voisins

def voisins_int(fichier):
	liste_voisins = []
	
	with open(fichier) as fp:
		for line in fp:
			if line != "\n":
				a,b = line.split()
				
				liste_voisins.append( (int(a),int(b)) )
	fp.close()
	
	return liste_voisins

def create_graph(data):
	G = nx.Graph()
	G.add_edges_from(data)
	
	return G




def main():
	G = nx.sudoku_graph()

	values = coloration2(G, 1)
	print(values)

	i = 1
	d = dict()
	for v in values:
		if not v in d.keys():
			d[v] = i
			i += 1
	print("nombre de couleur : {}".format(len(d.keys())))

	nx.draw(G, cmap=plt.get_cmap('viridis'), node_color=values, with_labels=True, font_color='white')
	plt.show()


if __name__ == '__main__':
	main()




