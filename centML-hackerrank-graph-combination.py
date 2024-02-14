'''
nodes are integers [0,...,n-1]
graphs are acyclic undirected represented by in_lists and out_list of numbers
eg. [1,2],[2,3] is
        1 - 2 - 3

given two graphs, find the pair of nodes, one on each graph, 
that when connecting the graphs, 
would give the minimum maximum depth of the super-graph

eg. for [1,2],[2,3] and [4,5],[5,6], connect at nodes 2 and 5
        1 - 2 - 3
           >|< -- the inserted edge
        4 - 5 - 6
   
return the maximum depth of the super-graph     
---
thoughts:
Observation: for either graph, the node with the minumum maximum distance is the node
    we will use later. Thus, a subproblem is finding the tree-depth-minimizing-root
    Then, we simply perform tree-depth-minimizing-root on both nodes. 
    But how? Perhaps via a bfs on each node?

'''

'''
I asked ChatGPT to provide stubs and test cases
'''
from collections import deque
def bfs_max_depth(start, adjacency_list):
    """
    Perform BFS to find the maximum depth from the start node.

    :param start: The starting node for BFS.
    :param adjacency_list: A dictionary representing the adjacency list of the graph.
    :return: The maximum depth from the start node.
    """
    visited = set()
    visited.add(start)
    q = deque()
    q.append((start, 0)) # (node, depth)
    ret = 0
    while q:
        current_node, depth = q.popleft()
        next_nodes = adjacency_list[current_node]
        ret = max(depth, ret)
        for neighbor in next_nodes:
            if neighbor not in visited:
                q.append((neighbor, depth + 1)) 
                ''' note depth addition here, above
                    note visited addition below
                '''
                visited.add(neighbor)
    return ret

def tree_depth_minimizing_root(in_list, out_list):
    """
    Find the root node that minimizes the maximum depth of the tree.

    :param in_list: A list of starting nodes for each edge.
    :param out_list: A list of ending nodes for each edge, corresponding to in_list.
    :return: A tuple of the best root node and its depth.
    """
    all_set = set(in_list + out_list)
    n = len(out_list)
    adjacency_list = {}
    for node in all_set:
        adjacency_list[node] = []
    for i in range(1,n+1):
        in_node = in_list[i-1]
        out_node = out_list[i-1]
        if in_node not in adjacency_list[out_node]:
            adjacency_list[out_node].append(in_node)
        if out_node not in adjacency_list[in_node]:
            adjacency_list[in_node].append(out_node)
    
    min_sf = n 
    ret_node = -1
    for node in all_set:
        node_max_depth = bfs_max_depth(node, adjacency_list)
        if min_sf > node_max_depth:
            min_sf = node_max_depth
            ret_node = node
    print(ret_node, min_sf)
    return ret_node, min_sf

def connect_graphs_minimize_depth(in_list1, out_list1, in_list2, out_list2):
    """
    Connect two graphs to minimize the maximum depth of the super-graph.

    :param in_list1: in_list for the first graph.
    :param out_list1: out_list for the first graph.
    :param in_list2: in_list for the second graph.
    :param out_list2: out_list for the second graph.
    :return: The maximum depth of the super-graph after connecting the two graphs.
    """
    nodeA, graphA_min_max_depth = tree_depth_minimizing_root(in_list1, out_list1)
    nodeB, graphB_min_max_depth = tree_depth_minimizing_root(in_list2, out_list2)
    sum = graphA_min_max_depth + graphB_min_max_depth
    print(sum)
    return sum + 1

# Test cases for bfs_max_depth
adjacency_list = {1: [2], 2: [1, 3], 3: [2]}
assert bfs_max_depth(1, adjacency_list) == 2, "Test case 1 failed"

adjacency_list = {1: [2, 3], 2: [1, 4, 5], 3: [1], 4: [2], 5: [2]}
assert bfs_max_depth(1, adjacency_list) == 2, "Test case 2 failed"

# Test cases for tree_depth_minimizing_root
assert tree_depth_minimizing_root([1, 2], [2, 3]) == (2, 1), "Test case 3 failed"
assert tree_depth_minimizing_root([1, 2, 3], [2, 3, 4]) == (2, 2), "Test case 4 failed"

# Test cases for connect_graphs_minimize_depth
assert connect_graphs_minimize_depth([1, 2], [2, 3], [4, 5], [5, 6]) == 3, "Test case 5 failed"
assert connect_graphs_minimize_depth([1, 2, 2], [2, 3, 4], [5, 6], [6, 7]) == 3, "Test case 6 failed"

