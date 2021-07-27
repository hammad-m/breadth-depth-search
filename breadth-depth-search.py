graph =  {
    'A' : ['B','C','D'],
    'B' : ['E', 'F'],
    'C' : [],
    'D' : [],
    'E' : ['G','H','I'],
    'F' : [],
    'G' : ['J'],
    'H' : [],
    'I' : [],
    'J' : []
}


def bdsutil(graph,b,startNode,visited):
    if startNode not in visited:
        visited.append(startNode)
    s=startNode
    if (len(graph[s]) > b):
        for neighbour in graph[s]:
            visited.append(neighbour)
            bdsutil(graph,b, neighbour,visited)    
    
    else:
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
        for neighbour in graph[s]:       
            bdsutil(graph,b, neighbour,visited)
    return " ".join(visited).strip()
    

def bds(graph, b, startNode):
    visited = []
    return  bdsutil(graph,b,startNode,visited)

print(bds(graph,2,'A'))
