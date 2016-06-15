def prim(graph):
    """Implementation of Prim's algorithm.
    """
    mst = set()
    current_node_set = set()
    current_node_set.add(graph.nodes()[0])
    while len(current_node_set) is not len(graph.nodes()):
        crossing = set()
        for node1 in current_node_set:
            for node2 in graph.nodes():
                if node2 not in current_node_set and graph[node1][node2]['weight'] is not 0:
                    crossing.add((node1, node2))
        edge = sorted(crossing, key=lambda e: graph[e[0]][e[1]]['weight'])[0]
        mst.add(edge)
        current_node_set.add(edge[1])
