'''
Let's use depth-first search to cover the basics of graphs.
Undirected Graph: A - B - C
    in adj list format
    { A: [B], B: [A, C], C: [B]}
    
    in adj matrix format
      A . B . C < TO
    A 0 . 1 . 0
    B 1 . 0 . 1
    C 0 . 1 . 0
    ^ FROM 
Directed Graph: A -> B -> C
    in adj list format: (from: [to])
    { A: [B], B: [C]}
    
    in adj matrix format
      A . B . C < TO
    A 0 . 1 . 0
    B 0 . 0 . 1
    C 0 . 0 . 0
    ^ FROM  

'''
from typing import Dict, List
from utils import print_matrix_row_by_row
graph_1 =  { "A": ["B"], "B": ["A", "C"], "C": ["B"]}
def convert_adjacency_list_to_adjacency_matrix(adjacency_list: Dict[str, List[str]]):
    vertices = list(adjacency_list.keys())
    n = len(vertices)
    matrix = []
    for i, v in enumerate(vertices):
        row = []
        for j, w in enumerate(vertices):
            # from v to w
            row.append( 1 if w in adjacency_list[v] else 0 )
        matrix.append(row)  
    return matrix

matrix_conversion_output = convert_adjacency_list_to_adjacency_matrix(graph_1)
print_matrix_row_by_row(matrix_conversion_output)

def convert_adjacency_matrix_to_adjacency_list(adjacency_matrix):
    n = len(adjacency_matrix)
    adj_lists = {}
    for i in range(n):
        for j in range(n):
            if adjacency_matrix[i][j]:
                adj_lists[i] = adj_lists.get(i, []) + [j]
    return adj_lists
print(convert_adjacency_matrix_to_adjacency_list(matrix_conversion_output))

def get_neighbours_from_adjacency_list(graph_as_adjacency_list, vertice):
    return graph_as_adjacency_list[vertice]
def get_neighbours_from_adjacency_matrix(graph_as_adjacency_matrix, vertice):
    pass # TODO

def dfs(graph_as_adj_list, starting_vertice = None):
    seen = set()
    if starting_vertice is None:
        starting_vertice = next(iter(graph_as_adj_list.keys()))
    def deep_dive(vertice):
        if vertice in seen:
            pass
        else:
            seen.add(vertice)
            print(vertice)
            neighbors = get_neighbours_from_adjacency_list(graph_as_adj_list, vertice)
            for neighbor in neighbors:
                deep_dive(neighbor)
    deep_dive(starting_vertice)

dfs(graph_1)