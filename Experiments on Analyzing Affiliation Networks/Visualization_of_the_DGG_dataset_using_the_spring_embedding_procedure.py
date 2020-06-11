import Data
import methods
import networkx as nx

G = methods.method_of_generate_graph.generate_graph(Data.people_list, Data.date_list, Data.relation_list)
methods.method_of_generate_graph.show_graph(G)

print('------------------------------------------------------------')
print('Is it a Bipartite:', nx.is_connected(G))
print('------------------------------------------------------------')
print("number_of_nodes:%s" % G.number_of_nodes())
print('------------------------------------------------------------')
print("number_of_edges:%s" % G.number_of_edges())
print('------------------------------------------------------------')
print("neighbors:%s" % G.adj)
print('------------------------------------------------------------')
print("degree:%s" % G.degree)
