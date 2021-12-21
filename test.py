import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
#G.add_node(1)
#G.add_nodes_from([2,3])
#G.add_edges_from([(0,1), (0,2), (1,3)])

G = nx.Graph()
#G.add_edge(1, 2)
#G.add_edge(1, 3)
#G.add_edge(1, 5)
#G.add_edge(2, 3)
#G.add_edge(3, 4)
#G.add_edge(4, 5)


G.add_edges_from([(1, 2),
				  (1, 3),
				  (1, 5),
				  (2, 3),
				  (3, 4),
				  (4, 5)
		 		 ])

pos = nx.spring_layout(G, seed=3113794652)
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=[(0, 1), (1, 2), (2, 3), (3, 0)],
    width=8,
    alpha=0.5,
    edge_color="tab:red",
)
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=[(4, 5), (5, 6), (6, 7), (7, 4)],
    width=8,
    alpha=0.5,
    edge_color="tab:blue",
)

nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
