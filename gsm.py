import sys
import networkx as nx
import matplotlib.pyplot as plt

from brouillon.coloration import *


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


def main(fl):
	data = voisins_int(fl)
	
	print(data)
	G = create_graph(data)
	
	print(coloration(G, 0))
	
	nx.draw(G, with_labels=True, font_weight='bold')
	plt.show()



if __name__ == '__main__':
	assert len(sys.argv) > 1, 'il manque un argument'
	main(sys.argv[1])




