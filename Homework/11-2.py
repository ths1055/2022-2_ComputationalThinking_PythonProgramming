from MyGraph import*

def initGraph(ICD_file_name):
    G = Digraph()
    ICD_file_name='KR_InterCityDist.txt'
    f=open(ICD_file_name,'r')
    data=f.readlines()
    f.close()
    data_processed=[]
    for d in data:
        data_processed.append(list(map(str,d.split())))
    n_names=[]
    lines=[]
    for i in range(len(data_processed)):
        lines.append(WeightedEdge(data_processed[i][0],data_processed[i][1],int(data_processed[i][2])))
        lines.append(WeightedEdge(data_processed[i][1],data_processed[i][0],int(data_processed[i][2])))
        for j in range(2):
            if data_processed[i][j] not in n_names:
                n_names.append(data_processed[i][j])
    print('initGraph() - adding nodes into Graph : ',end='')
    for i in range(len(n_names)):
        v_name = n_names[i]
        node = Node(v_name)
        print(f'{node.getName()}, ',end='')
        #print("initGraph() :: adding node ({}) into Graph".format(node.getName()))
        G.addNode(node)
    print()
    for we in lines:
        #print("\ninitGraph() :: adding weighted_edge {} into Graph".format(we))
        G.addEdge(we)
    return G
EdgesPerLine = 5

if __name__ == "__main__":
    G = initGraph("KR_InterCityDist.txt")
    node_names = G.getNode_NMs()
    print("Nodes : ", node_names)
    edges = G.getWEdges()
    print("Edges :")
    eCount = 0
    for e in edges:
        print(" {}".format(e), end=', ')
        eCount += 1
        if eCount % EdgesPerLine == 0:
            print()
    print()
    #print("\nInter-City Connectivity Table:")
    G.printConnectivity()
    #print("weightedEdges : ", G.getWeightedEdges())
    start_nm = "GJ" # G.nodes[7].getName()
    end_nm = "SC" # G.nodes[2].getName()
    print("Trying ShortestPath_Dijkstra : ({} -> {})".format(start_nm, end_nm))
    path_Dijkstra, path_cost = Dijkstra(G, start_nm, end_nm)
    print("Found shortestPath_Dijkstra ({} -> {}): {}, total_path_cost ={}".format(start_nm, end_nm, path_Dijkstra, path_cost))
    start_nm = "SC" # G.nodes[7].getName()
    end_nm = "GJ" # G.nodes[2].getName()
    print("Trying ShortestPath_Dijkstra : ({} -> {})".format(start_nm, end_nm))
    path_Dijkstra, path_cost = Dijkstra(G, start_nm, end_nm)
    print("Found shortestPath_Dijkstra ({} -> {}): {}, total_path_cost ={}".format(start_nm, end_nm, path_Dijkstra, path_cost))