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
				rendu = line.split()
				liste_voisins.append(tuple(rendu))
	fp.close()
	
	return liste_voisins


def create_graph(data):
	d = dict()
	comp = 0
	for v1,v2 in data:
		if not v1 in d.keys():
			d[v1] = comp
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
	G = create_graph(data)
	
	values = coloration(G, 0)
	
	nx.draw(G, with_labels=True, font_weight='bold')

	#nx.draw(G, cmap=plt.get_cmap('viridis'), node_color=values, with_labels=True, font_color='white')
	plt.show()
	
if __name__ == '__main__':
	assert len(sys.argv) > 1, 'il manque un argument'
	main(sys.argv[1])




