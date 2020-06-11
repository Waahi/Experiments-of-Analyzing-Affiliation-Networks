import Data
import methods


H = methods.method_of_generate_graph.generate_graph(Data.people_list, Data.date_list, Data.relation_list)

Ties_number = sorted(
    methods.method_of_Ties.Num_of_Ties(Data.people_list, Data.date_list, Data.relation_list, Data.all_list).items(),
    key=lambda x: x[1], reverse=True)
Degree = sorted(methods.centrality_method.degree_centrality(H, Data.people_list).items(), key=lambda x: x[1],
                reverse=True)
Closeness = sorted(methods.centrality_method.closeness_centrality(H, Data.people_list).items(), key=lambda x: x[1],
                   reverse=True)
Betweenness = sorted(methods.centrality_method.betweenness_centrality(H, Data.people_list).items(), key=lambda x: x[1],
                     reverse=True)
Eigenvector = sorted(methods.centrality_method.eigenvector_centrality(H).items(), key=lambda x: x[1], reverse=True)

list_A = [Ties_number, Degree, Closeness, Betweenness, Eigenvector]
list_B = ['Ties_number', 'Degree', 'Closeness', 'Betweenness', 'Eigenvector']
list_C = [Degree, Closeness, Betweenness, Eigenvector]

Everage = methods.centrality_method.average_of_centrality(Data.all_list, list_C)

for i in list_A:
    print('Number of %s is %d' % (list_B[list_A.index(i)], len(i)), '%s :' % i)
    print('------------------------------------------------------------')
    print('------------------------------------------------------------')
print(Everage)

import numpy as np
import pandas as pd

scores_graph = np.zeros((len(Data.all_list) + 1, 6))
scores_graph = scores_graph.astype(np.str)

for i in range(0, len(Data.list_D)):
    scores_graph[0][i] = Data.list_D[i]

for i in range(1, len(Data.all_list) + 1):
    scores_graph[i][0] = Betweenness[i - 1][0]

for i in list_A:
    for j in range(0, len(Data.all_list)):
        for k in range(0, len(i)):
            if scores_graph[j + 1][0] == i[k][0]:
                scores_graph[j + 1][list_A.index(i) + 1] = i[k][1]

S_G = pd.DataFrame(scores_graph)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 1000)
pd.set_option('expand_frame_repr', False)
print(S_G)

'''
normalization of Ties maybe can be used for analysis

Normalized_T = methods.centrality_method.nomalization(Ties_number)
list_C = [Normalized_T, Degree, Closeness, Betweenness, Eigenvector]
Everage = methods.centrality_method.average_of_centrality(Data.all_list, list_D)

'''
