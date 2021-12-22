import sys
import networkx as nx
import matplotlib.pyplot as plt

from brouillon.coloration import *

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
				rendu = line.split()
				liste_voisins.append(tuple(rendu))
	fp.close()
	
	return liste_voisins


def attribut_entier_au_pays:
	

def create_graph(data):
	d = dict()
	comp = 0
	for v1,v2 in data:
		if not v1 in d.keys():
			d[v] = comp
			comp +=1
		if not v2 in d.keys():
			d[v2] = comp
			comp += 1
	print(d)
	G = nx.Graph()
	G.add_edges_from(data)
	
	return G




def main(fl):
	data = voisins(fl)
	print(data)
	G = create_graph(data)
	
	print(coloration(G, 0))
	
	nx.draw(G, with_labels=True, font_weight='bold')
	plt.show()
	
if __name__ == '__main__':
	assert len(sys.argv) > 1, 'il manque un argument'
	main(sys.argv[1])




