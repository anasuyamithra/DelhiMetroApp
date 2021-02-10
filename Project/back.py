from main import *

''' creating a graph class '''

import networkx as nx
ntx_graph = nx.Graph()

class Graph(object):

   def __init__(self):
       self.nodes = {}
       self.edges = {}
       self.distances = {}
       self.key_to_name = {}
       self.path = []
       self.path_time = 0
       self.path_len = 0
       self.path_changes = 0
       self.all_paths = {}
       self.all_paths_wts = {}

   def add_vertex(self, value, name):
       ntx_graph.add_node(value)
       self.nodes[value] = name
       self.key_to_name[name] = value

   def add_edge(self, from_node, to_node, distance):
       self._add_edge(from_node, to_node, distance)
       self._add_edge(to_node, from_node, distance)

   def _add_edge(self, from_node, to_node, distance):
       ntx_graph.add_edge(from_node, to_node, weight=distance)
       self.edges.setdefault(from_node, [])
       self.edges[from_node].append(to_node)
       self.distances[(from_node, to_node)] = distance




''' djikstra function definition '''


def dijkstra(graph, initial_node):
    visited = {initial_node: 0}
    current_node = initial_node
    path = {}
    
    unvisited = set(graph.nodes)

    while unvisited:
        min_node = None
        for node in unvisited:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        unvisited.remove(min_node)
        cur_wt = visited[min_node]

        for edge in graph.edges[min_node]:
            wt = cur_wt + graph.distances[(min_node, edge)]
            if edge not in visited or wt < visited[edge]:
                visited[edge] = wt
                path[edge] = min_node

    return visited, path

''' recursive function to get route '''

def route(graph, x, y):
    distances, paths = dijkstra(graph, x)


    route = [y]

    while y != x:
        route.append(paths[y])
        y = paths[y]


    route.reverse()
    return route

''' function to get route and assign colours according to line changes '''

def print_route(graph, x, y):
        r = route(graph, x, y)
        g.path_len = len(r)
        u = int(x)
        line_changes = {}
        key_to_line_changes = {}
        i = 0



        
        prmpt = list()
        for y in r[1:]:

            if x >=0 and x <= 27:
                    if x == 11 and (y == 98 or y == 96):
                        c = 3
                        key_to_line_changes[i] = c
                        
                    elif x == 14 and (y == 40 or y == 38):
                        c = 2
                        
                        key_to_line_changes[i] = c
                        
                    elif x == 14 and (y == 204):
                        
                        
                        c = 8
                        
                        key_to_line_changes[i] = c

                    elif x == 19 and (y == 169):
                        
                        
                        c = 6
                        
                        key_to_line_changes[i] = c
                        
                        
                    elif x == 22 and (y == 67 or y == 69):
                        
                        
                        c = 3
                        
                        key_to_line_changes[i] = c
                    else:
                        c = 1
                        key_to_line_changes[i] = c
      
            elif x >= 28 and x <= 64:

                    if x == 33 and (y == 67 or y == 65):
                        c = 3
                        
                        key_to_line_changes[i] = c
                        
                        
                        
                    elif x == 42 and (y == 163):
                       
                        c = 5
                        
                        key_to_line_changes[i] = c
                        
                        
                    elif x == 49 and (y == 81 or y == 79):
                        
                        c = 3
                        
                        key_to_line_changes[i] = c
                        
                        
                    elif x == 43 and (y == 131 or y == 133):
                        
                       
                        c = 4
                        
                        key_to_line_changes[i] = c
                        
                        
                    elif x == 45 and (y == 209 or y == 211):
                       
                        c = 8
                        
                        key_to_line_changes[i] = c
                        
                        
                    elif x == 52 and (y == 247 or y == 249):
                        
                        c = 9
                        
                        key_to_line_changes[i] = c
                        
                        
                    elif x == 61 and (y == 196 or y == 198):
                        
                        c = 7
                        
                        key_to_line_changes[i] = c
                    else:
                        c = 2
                        key_to_line_changes[i] = c

            elif x >= 65 and x <= 102:
                    if x == 72 and (y == 120 or y == 122):
                       
                        c = 4
                        
                        key_to_line_changes[i] = c
                       
                        
                    if x == 82 and (y == 213 or y == 215):
                        
                        c = 8
                        
                        key_to_line_changes[i] = c
                        
                        
                    if x == 86 and (y == 138 or y == 140):
                        
                        c = 4
                        
                        key_to_line_changes[i] = c
                        
                        
                    if x == 92 and (y == 157 or y == 93):
                        
                        c = 4
                        
                        key_to_line_changes[i] = c
                       
                        
                    if x == 93 and (y == 92 or y == 160):
                    
                        c = 4
                        
                        key_to_line_changes[i] = c
                    else:
                        c = 3
                        key_to_line_changes[i] = c
                        
            elif x >= 103 and x <= 153:
                    if x == 103 and (y == 166):
                        
                        c = 5
                        
                        key_to_line_changes[i] = c
                        
                        
                    if x == 111 and (y == 284):
                        
                        c = 11
                        
                        key_to_line_changes[i] = c
                        
                        
                    if x == 134 and (y == 207 or y ==209):
                       
                        c = 8
                       
                        key_to_line_changes[i] = c

                        
                    if x == 125 and (y == 190):
                       
                        c = 6
                        
                        key_to_line_changes[i] = c
                       
                        
                    if x == 116 and (y == 238):
                       
                        c = 9
                        
                        key_to_line_changes[i] = c
                        
                        
                    if x == 137 and (y == 155):
                       
                        c = 4
                        
                        key_to_line_changes[i] = c    
                        
                    if x == 145 and (y == 260):
                       
                        c = 9
                        
                        key_to_line_changes[i] = c
                        
                        
                    if x == 149 and (y == 263):
                        
                        c = 10
                        
                        key_to_line_changes[i] = c
                    else:
                        c = 4
                        key_to_line_changes[i] = c
            
            elif x >= 154 and x <= 161:
                c = 4
                key_to_line_changes[i] = c
            elif x >= 162 and x <= 167:
                c = 5
                key_to_line_changes[i] = c
            elif x >= 168 and x <= 188:
                    if x == 169 and (y == 190):
                        c = 6
                        
                        key_to_line_changes[i] = c
                    else:
                        c = 6
                        key_to_line_changes[i] = c
                        
                
            elif x >= 189 and x <= 191:
                c = 6
                key_to_line_changes[i] = c
            elif x >= 192 and x <= 202:
                c = 7
                key_to_line_changes[i] = c
            elif x >= 203 and x <= 236:
                    if x == 218 and (y == 252 or y == 254):
                        c = 9
                        
                        key_to_line_changes[i] = c
                        
                    else:
                        c = 8
                        key_to_line_changes[i] = c
                
            elif x >= 237 and x <= 261:
                c = 9
                key_to_line_changes[i] = c
            elif x >= 262 and x <= 282:
                c = 10
                key_to_line_changes[i] = c
            elif x >= 283 and x <= 285:
                c = 11
                key_to_line_changes[i] = c
            else:
                print("error in laying out colours for initial node")

            line_changes.setdefault(c,[])

            d = graph.distances.get((x, y))
            g.path_time = g.path_time + d

            if g.nodes[x] is not 'blank':
                prmpt.append('{}'.format(g.nodes[x]))
            try:
                
                
                if u >=0 and u <=27:
                    if x == 11 and (y == 98 or y == 96):
                        print("\nLine change: RED TO PINK\n")
                        u = 98
                        c = 3
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 14 and (y == 40 or y == 38):
                        print("\nLine change: RED TO YELLOW\n")
                        u = 40
                        c = 2
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 14 and (y == 204):
                        print("\nLine change: RED TO VIOLET\n")
                        u = 204
                        c = 8
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        

                    if x == 19 and (y == 169):
                        print("\nLine change: RED TO GREEN\n")
                        u = 169
                        c = 6
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 22 and (y == 67 or y == 69):
                        print("\nLine change: RED TO PINK\n")
                        u = 69
                        c = 3
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                elif u >=28 and u <=64: 
                    if x == 14 and (y == 13 or y == 15):                              
                        print("\nLine change: YELLOW TO RED\n")
                        u = 15
                        c = 1
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 33 and (y == 67 or y == 65):
                        print("\nLine change: YELLOW TO PINK\n")
                        u = 67
                        c = 3
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 14 and (y == 204):
                        print("\nLine change: YELLOW TO VIOLET\n")
                        u = 204
                        c = 8
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 42 and (y == 163):
                        print("\nLine change: YELLOW TO ORANGE\n")
                        u = 163
                        c = 5
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 49 and (y == 81 or y == 79):
                        print("\nLine change: YELLOW TO PINK\n")
                        u = 81
                        c = 3
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 43 and (y == 131 or y == 133):
                        print("\nLine change: YELLOW TO BLUE\n")
                        u = 131
                        c = 4
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 45 and (y == 209 or y == 211):
                        print("\nLine change: YELLOW TO VIOLET\n")
                        u = 209
                        c = 8
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 52 and (y == 247 or y == 249):
                        print("\nLine change: YELLOW TO MAGENTA\n")
                        u = 247
                        c = 9
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 61 and (y == 196 or y == 198):
                        print("\nLine change: YELLOW TO RAPID\n")
                        u = 196
                        c = 7
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                elif u >=65 and u <=102: 
                    if x == 33 and (y == 32 or y == 34):
                        print("\nLine change: PINK TO YELLOW\n")
                        u = 34
                        c = 2
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 49 and (y == 48 or y == 50):
                        print("\nLine change: PINK TO YELLOW\n")
                        u = 50
                        c = 2
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 11 and (y == 10 or y == 12):
                        print("\nLine change: PINK TO RED\n")
                        u = 12
                        c = 1
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 22 and (y == 21 or y == 23):
                        print("\nLine change: PINK TO RED\n")
                        u = 23
                        c = 1
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 72 and (y == 120 or y == 122):
                        print("\nLine change: PINK TO BLUE\n")
                        u = 120
                        c = 4
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 82 and (y == 213 or y == 215):
                        print("\nLine change: PINK TO VIOLET\n")
                        u = 213
                        c = 8
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 86 and (y == 138 or y == 140):
                        print("\nLine change: PINK TO BLUE\n")
                        u = 23
                        c = 4
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 92 and (y == 157 or y == 93):
                        print("\nLine change: PINK TO BLUE BRANCH 2\n")
                        u = 157
                        c = 4
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 93 and (y == 92 or y == 160):
                        print("\nLine change: PINK TO BLUE BRANCH 2\n")
                        u = 160   
                        c = 4
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                                                         #confusion how to code this + found a bug, try indraprastha to vaishali
                elif u >=103 and u <=153: 
                    if x == 103 and (y == 166):
                        print("\nLine change: BLUE TO ORANGE\n")
                        u = 166
                        c = 5
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 111 and (y == 284):
                        print("\nLine change: BLUE TO GRAY\n")
                        u = 284
                        c = 11
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 134 and (y == 207 or y ==209):
                        print("\nLine change: BLUE TO VIOLET\n")
                        u = 166 
                        c = 8
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 72 and (y == 71 or y == 73):
                        print("\nLine change: BLUE TO PINK\n")
                        u = 71
                        c = 3
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 125 and (y == 190):
                        print("\nLine change: BLUE TO GREEN BRANCH 2\n")
                        u = 190 
                        c = 6
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 43 and (y == 42 or y == 44):
                        print("\nLine change: BLUE TO YELLOW\n")
                        u = 42
                        c = 2
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 116 and (y == 238):
                        print("\nLine change: BLUE to MAGENTA\n")
                        u = 238 
                        c = 9
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 137 and (y == 155):
                        print("\nLine change: BLUE TO BLUE BRANCH 2\n")
                        u = 155
                        c = 4
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 86 and (y == 85 or y == 87):
                        print("\nLine change: BLUE TO PINK\n")  
                        u = 87
                        c = 3
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 145 and (y == 260):
                        print("\nLine change: BLUE TO MAGENTA\n")
                        u = 260
                        c = 9
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 149 and (y == 263):
                        print("\nLine change: BLUE TO AQUA\n")
                        u = 263
                        c = 10
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                elif u >=154 and u <=161: 
                    if x == 137 and (y == 136 or y == 138):
                        print("\nLine change: BLUE BRANCH 2 TO BLUE\n")
                        u = 166
                        c = 4
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 92 and (y == 91 or y == 93):
                        print("\nLine change: BLUE BRANCH 2 TO PINK\n")
                        u = 91
                        c = 3
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 93 and (y == 92 or y ==94):
                        print("\nLine change: BLUE BRANCH 2 TO PINK\n")
                        u = 94 
                        c = 3
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                elif u >=162 and u <=167: 
                    if x == 103 and (y == 104):
                        print("\nLine change: ORANGE TO BLUE\n")
                        u = 104
                        c = 4
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 42 and (y == 43 or y == 41):
                        print("\nLine change: ORANGE TO YELLOW\n")
                        u = 284
                        c = 2
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                elif u >=168 and u <=188: 
                    if x == 19 and (y == 18 or y == 20):
                        print("\nLine change: GREEN TO RED\n")
                        u = 18
                        c = 1
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 169 and (y == 190):
                        print("\nLine change: GREEN TO GREEN BRANCH 2\n")
                        u = 190
                        c = 6
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                elif u >=189 and u <=191: 
                    if x == 169 and (y == 19 or y == 170):
                        print("\nLine change: GREEN BRANCH 2 TO GREEN\n")
                        u = 170
                        c = 6
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 125 and (y == 124 or y == 126):
                        print("\nLine change: GREEN BRANCH 2 TO BLUE\n")
                        u = 124
                        c = 4
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                elif u >=192 and u <=202: 
                    if x == 61 and (y == 60 or y == 62):
                        print("\nLine change: RAPID TO YELLOW\n")
                        u = 60
                        c = 2
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                elif u >=203 and u <=236: 
                    if x == 14 and (y == 13 or y == 15):
                        print("\nLine change: VIOLET TO RED\n")
                        u = 13
                        c = 1
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 14 and (y == 40 or y == 38):
                        print("\nLine change: VIOLET TO YELLOW\n")
                        u = 38
                        c = 2
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 134 and (y == 133 or y ==135):
                        print("\nLine change: VIOLET TO BLUE\n")
                        u = 133 
                        c = 4
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 45 and (y == 44 or y == 46):
                        print("\nLine change: VIOLET TO YELLOW\n")
                        u = 44
                        c = 2
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 82 and (y == 81 or y == 83):
                        print("\nLine change: VIOLET TO PINK\n")
                        u = 81
                        c = 3
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 218 and (y == 252 or y == 254):
                        print("\nLine change: VIOLET TO MAGENTA\n")
                        u = 252
                        c = 9
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                elif u >=237 and u <=261: 
                    if x == 116 and (y == 115 or y == 117):
                        print("\nLine change: MAGENTA to BLUE\n")
                        u = 115
                        c = 4
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 52 and (y == 51 or y == 53):
                        print("\nLine change: MAGENTA TO YELLOW\n")
                        u = 51
                        c = 2
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 218 and (y == 217 or y ==219):
                        print("\nLine change: MAGENTA TO VIOLET\n")
                        u = 217 
                        c = 8
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                    if x == 145 and (y == 144 or y == 146):
                        print("\nLine change: MAGENTA TO BLUE\n")
                        u = 144
                        c = 4
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                elif u >=262 and u <=282: 
                    if x == 149 and (y == 150 or y == 148):
                        print("\nLine change: AQUA TO BLUE\n")
                        u = 148
                        c = 4
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                elif u >=283 and u <=285: 
                    if x == 111 and (y == 110 or y == 112):
                        print("\nLine change: GREY TO BLUE\n")
                        u = 110
                        c = 4
                        placeholder = 0
                        key_to_line_changes[i] = c
                        g.path_changes = g.path_changes + 1
                        
                i = i + 1
                key_to_line_changes[i] = c
            except:
                print("Error in print function in back.py")
            x = y
        prmpt.append('{}'.format(g.nodes[y]))
        
        g.path.extend(prmpt)   #adds prompt to the path list

        return prmpt, key_to_line_changes


g = Graph()

# RED LINE    1


g.add_vertex(0, 'Shaheed Sthal(New Bus Adda)')
g.add_vertex(1, 'Hindon River')
g.add_vertex(2, 'Arthala')
g.add_vertex(3, 'Mohan Nagar')
g.add_vertex(4, 'Major Mohit Sharma')
g.add_vertex(5, 'Raj Bagh')
g.add_vertex(6, 'Shaheed Nagar')
g.add_vertex(7, 'Dilshad Garden')
g.add_vertex(8, 'Jhil Mil')
g.add_vertex(9, 'Mansarovar Park')
g.add_vertex(10, 'Shahdara')
g.add_vertex(11, 'Welcome')  #Conn: Pink
g.add_vertex(12, 'Seelampur')
g.add_vertex(13, 'Shastri Park')
g.add_vertex(14, 'Kashmere Gate') #Conn: Violet Conn: Yellow 
g.add_vertex(15, 'Tis Hazari')
g.add_vertex(16, 'Pul Bangash')
g.add_vertex(17, 'Pratap Nagar')
g.add_vertex(18, 'Shastri Nagar')
g.add_vertex(19, 'Inderlok') #Conn: Green
g.add_vertex(20, 'Kanhaiya Nagar')
g.add_vertex(21, 'Keshav Puram')
g.add_vertex(22, 'Netaji Subash Place') #Conn: Pink
g.add_vertex(23, 'Kohat Enclave')
g.add_vertex(24, 'Pitam Pura')
g.add_vertex(25, 'Rohini East')
g.add_vertex(26, 'Rohini West')
g.add_vertex(27, 'Rithala')

#  YELLOW LINE     2

g.add_vertex(28, 'Samaypur Badli')
g.add_vertex(29, 'Rohini Sector 18-19')
g.add_vertex(30, 'Haiderpur Badli Mor')
g.add_vertex(31, 'Jahangirpuri')
g.add_vertex(32, 'Adarsh Nagar')
g.add_vertex(33, 'Azadpur') # Conn: Pink
g.add_vertex(34, 'Model Town')
g.add_vertex(35, 'Guru Tegh Bahadur Nagar')
g.add_vertex(36, 'Vishwavidyalaya')
g.add_vertex(37, 'Vidhan Sabha')
g.add_vertex(38, 'Civil Lines')
#g.add_vertex(39, 'Kashmere Gate') #Conn: Violet Conn: Red  14
g.add_vertex(40, 'Chandni Chowk')
g.add_vertex(41, 'LusaChawri Bazaril')
g.add_vertex(42, 'New Delhi') #Conn: Orange
g.add_vertex(43, 'Rajiv Chowk') #Conn: Blue
g.add_vertex(44, 'Patel Chowk')
g.add_vertex(45, 'Central Secretariat') #Conn: Violet
g.add_vertex(46, 'Udyog Bhawan')
g.add_vertex(47, 'Lok Kalyan Marg')
g.add_vertex(48, 'Jorbagh')
g.add_vertex(49, 'Dilli Haat INA') #Conn: Pink
g.add_vertex(50, 'AIIMS')
g.add_vertex(51, 'Green Park')
g.add_vertex(52, 'Hauz Khas') #Conn: Magenta
g.add_vertex(53, 'Malviya Nagar')
g.add_vertex(54, 'Saket')
g.add_vertex(55, 'Qutab Minar')
g.add_vertex(56, 'Chhattarpur')
g.add_vertex(57, 'Sultanpur')
g.add_vertex(58, 'Ghitorni')
g.add_vertex(59, 'Arjan Garh')
g.add_vertex(60, 'Guru Dronacharya')
g.add_vertex(61, 'Sikandarpur') #Conn: Rapid
g.add_vertex(62, 'MG Road')
g.add_vertex(63, 'IFFCO Chowk')
g.add_vertex(64, 'Huda City Centre')

# PINK LINE    3

g.add_vertex(65, 'Majlis Park')
#g.add_vertex(66, 'Azadpur') #Conn: Yellow 33
g.add_vertex(67, 'Shalimar Bagh')
#g.add_vertex(68, 'Netaji Subash Place') #Conn: Red 22
g.add_vertex(69, 'Shakurpur')
g.add_vertex(70, 'Punjabi Bagh West')
g.add_vertex(71, 'ESI BASAI DARAPUR')
g.add_vertex(72, 'Rajouri Garden') #Conn: Blue
g.add_vertex(73, 'Maya Puri')
g.add_vertex(74, 'Naraina Vihar')
g.add_vertex(75, 'Delhi Cantt')
g.add_vertex(76, 'Durgabai Deshmukh South Campus') 
g.add_vertex(77, 'Sir Vishweshwaraiah Moti Bagh')
g.add_vertex(78, 'Bhikaji Cama Place')
g.add_vertex(79, 'Sarojini Nagar')
#g.add_vertex(80, 'Dilli Haat INA') #Conn: Yellow 49
g.add_vertex(81, 'South Extension')
g.add_vertex(82, 'Lajpat Nagar') #Conn: Violet
g.add_vertex(83, 'Vinobapuri')
g.add_vertex(84, 'Ashram')
g.add_vertex(85, 'Sarai Kale Khan Hazrat Nizamuddin')
g.add_vertex(86, 'Mayur Vihar Phase-1') #Conn: Blue
g.add_vertex(87, 'Mayur Vihar Pocket I')
g.add_vertex(88, 'Trilokpuri Sanjay Lake')
g.add_vertex(89, 'Vinod Nagar East')
g.add_vertex(90, 'Mandawali - West Vinod Nagar')
g.add_vertex(91, 'IP Extension')
g.add_vertex(92, 'Anand Vihar') #Conn: Blue
g.add_vertex(93, 'Karkar Duma') #Conn: Blue
g.add_vertex(94, 'Karkarduma Court')
g.add_vertex(95, 'Krishna Nagar')
g.add_vertex(96, 'East Azad Nagar')
#g.add_vertex(97, 'Welcome') #Conn: Red, 11
g.add_vertex(98, 'Jaffrabad')
g.add_vertex(99, 'Maujpur')
g.add_vertex(100, 'Gokulpuri')
g.add_vertex(101, 'Johri Enclave')
g.add_vertex(102, 'Shiv Vihar')


# BLUE LINE    4

g.add_vertex(103, 'Dwarka Sector 21') #conn : Orange
g.add_vertex(104, 'Dwarka Sector 8')
g.add_vertex(105, 'Dwarka Sector 9')
g.add_vertex(106, 'Dwarka Sector 10')
g.add_vertex(107, 'Dwarka Sector 11')
g.add_vertex(108, 'Dwarka Sector 12')
g.add_vertex(109, 'Dwarka Sector 13')
g.add_vertex(110, 'Dwarka Sector 14')
g.add_vertex(111, 'Dwarka') #conn : grey
g.add_vertex(112, 'Dwarka Mor')
g.add_vertex(113, 'Nawada')
g.add_vertex(114, 'Uttam Nagar West')  
g.add_vertex(115, 'Uttam Nagar East')
g.add_vertex(116, 'Janak Puri West') #conn: blue
g.add_vertex(117, 'Janak Puri East')
g.add_vertex(118, 'Tilak Nagar')
g.add_vertex(119, 'Subhash Nagar') 
g.add_vertex(120, 'Tagore Garden')
#g.add_vertex(121, 'Rajouri Garden') #conn :pink 72
g.add_vertex(122, 'Ramesh Nagar') 
#g.add_vertex(123, 'Kohat Enclave')
g.add_vertex(124, 'Moti Nagar')
g.add_vertex(125, 'Kirti Nagar') #conn : green
g.add_vertex(126, 'Shadipur')
g.add_vertex(127, 'Patel Nagar')
g.add_vertex(128, 'Rajendra Place')
g.add_vertex(129, 'Karol Bagh')
g.add_vertex(130, 'Jhandewalan')
g.add_vertex(131, 'R K Ashram Marg')
#g.add_vertex(132, 'Rajiv Chowk') #Conn : yellow 43
g.add_vertex(133, 'Barakhamba')
g.add_vertex(134, 'Mandi House') #conn : violet
g.add_vertex(135, 'Supreme Court (Pragati Maidan)')
g.add_vertex(136, 'Indraprastha')
g.add_vertex(137, 'Yamuna Bank') #conn :second branch of blue line
g.add_vertex(138, 'Akshardham')
#g.add_vertex(139, 'Mayur Vihar Phase-1') #conn :pink 86
g.add_vertex(140, 'Mayur Vihar Extention')
g.add_vertex(141, 'New Ashok Nagar')
g.add_vertex(142, 'Noida Sector 15') 
g.add_vertex(143, 'Noida Sector 16') 
g.add_vertex(144, 'Noida Sector 18')
g.add_vertex(145, 'Botanical Garden') #conn : magenta
g.add_vertex(146, 'Golf Course')
g.add_vertex(147, 'Noida City Center')
g.add_vertex(148, 'Noida Sector 34')
g.add_vertex(149, 'Noida Sector 52') #conn: aqua
g.add_vertex(150, 'Noida Sector 61')
g.add_vertex(151, 'Noida Sector 59')
g.add_vertex(152, 'Noida Sector 62')
g.add_vertex(153, 'Noida Electronic City')

#second branch of blue line

#g.add_vertex(154, 'Yamuna Bank') blue 137
g.add_vertex(155, 'Laxmi Nagar')
g.add_vertex(156, 'Nirman Vihar')
g.add_vertex(157, 'Preet Vihar')
#g.add_vertex(158, 'Karkar Duma') #conn : pink 92
#g.add_vertex(159, 'Anand Vihar') #conn : pink 93
g.add_vertex(160, 'Kaushambi')
g.add_vertex(161, 'Vaishali') 


# ORANGE LINE   5

#g.add_vertex(162, 'New Delhi') #conn : yellow 42
g.add_vertex(163, 'Shivaji Stadium')
g.add_vertex(164, 'Dhaula Kuan') 
g.add_vertex(165, 'Delhi Aerocity')
g.add_vertex(166, 'IGI Airport') 
#g.add_vertex(167, 'Dwarka Sector 21') #conn : Blue 103


#GREEN LINE   6

#g.add_vertex(168, 'Inderlok') #conn : RED 19
g.add_vertex(169, 'Ashok Park Main') #conn : other branch of green line
g.add_vertex(170, 'Punjabi Bagh')
g.add_vertex(171, 'Shivaji Park')
g.add_vertex(172, 'Madipur') 
g.add_vertex(173, 'Paschim Vihar (East)')
g.add_vertex(174, 'Paschim Vihar (West)')
g.add_vertex(175, 'Peera Garhi')
g.add_vertex(176, 'Udyog Nagar') 
g.add_vertex(177, 'Maharaja Surajmal Stadium')
g.add_vertex(178, 'Nangloi')
g.add_vertex(179, 'Nangloi Railway Station')
g.add_vertex(180, 'Rajdhani Park') 
g.add_vertex(181, 'Mundka')
g.add_vertex(182, 'Mundka Industrial Area (MIA)') 
g.add_vertex(183, 'Ghevra Metro station')
g.add_vertex(184, 'Tikri Kalan')
g.add_vertex(185, 'Tikri Border')
g.add_vertex(186, 'Pandit Shree Ram Sharma') 
g.add_vertex(187, 'Bahdurgarh City')
g.add_vertex(188, 'Brigadier Hoshiar Singh')

#other branch of green line

#g.add_vertex(189, 'Ashok Park Main') 169
g.add_vertex(190, 'Satguru Ram Singh Marg')
#g.add_vertex(191, 'Kirti Nagar') #conn : blue 125


#RAPID LINE    7
g.add_vertex(192, 'Sector 55-66') 
g.add_vertex(193, 'Sector 54 Chowk') 
g.add_vertex(194, 'Sector 53-54')
g.add_vertex(195, 'Sector 42-43')
g.add_vertex(196, 'DLF Phase 1')
#g.add_vertex(197, 'Sikandarpur') #Conn: Yellow 61
g.add_vertex(198, 'DLF Phase 2')
g.add_vertex(199, 'Belvedere Towers')
g.add_vertex(200, 'Cyber City')
g.add_vertex(201, 'Moulsari Avenue')
g.add_vertex(202, 'DLF Phase 3')

#VIOLET LINE   8

#g.add_vertex(203, 'Kashmere Gate') #conn : yellow , red 14
g.add_vertex(204, 'Lal Quila')
g.add_vertex(205, 'Jama Masjid')
g.add_vertex(206, 'Delhi Gate')
g.add_vertex(207, 'ITO')
#g.add_vertex(208, 'Mandi House') #conn : blue 134
g.add_vertex(209, 'Janpath')
#g.add_vertex(210, 'Central Secretariat') #conn: yellow 45
g.add_vertex(211, 'Khan Market') 
g.add_vertex(212, 'Jawaharlal Nehru Stadium')
g.add_vertex(213, 'Jangpura')
#g.add_vertex(214, 'Lajpat Nagar')  #conn:pink 82
g.add_vertex(215, 'Moolchand')
g.add_vertex(216, 'Kailash Colony') 
g.add_vertex(217, 'Nehru Place')
g.add_vertex(218, 'Kalkaji Mandir') #conn: magenta
g.add_vertex(219, 'Govind Puri') 
g.add_vertex(220, 'Okhla')
g.add_vertex(221, 'Jasola')
g.add_vertex(222, 'Sarita Vihar') 
g.add_vertex(223, 'Mohan Estate')
g.add_vertex(224, 'Tughlakabad')
g.add_vertex(225, 'Badarpur Border')
g.add_vertex(226, 'Sarai')
g.add_vertex(227, 'N.H.P.C. Chowk')
g.add_vertex(228, 'Mewala Maharajpur')
g.add_vertex(229, 'Sector 28 Faridabad')
g.add_vertex(230, 'Badkal Mor')
g.add_vertex(231, 'Old Faridabad')
g.add_vertex(232, 'Neelam Chowk Ajronda') 
g.add_vertex(233, 'Bata Chowk')
g.add_vertex(234, 'Escorts Mujesar') 
g.add_vertex(235, 'Sant Surdas - Sihi')
g.add_vertex(236, 'Raja Nahar Singh')


#MAGENTA LINE    9

#g.add_vertex(237, 'Janak Puri West') #conn: blue 116
g.add_vertex(238, 'Dabri Mor - Janakpuri South')
g.add_vertex(239, 'Dashrath Puri')
g.add_vertex(240, 'Palam')
g.add_vertex(241, 'Sadar Bazaar Cantonment')
g.add_vertex(242, 'Terminal 1 IGI Airport') 
g.add_vertex(243, 'Shankar Vihar') 
g.add_vertex(244, 'Vasant Vihar')
g.add_vertex(245, 'Munirka')
g.add_vertex(246, 'RK Puram')
g.add_vertex(247, 'IIT Delhi')
#g.add_vertex(248, 'Hauz Khas') #conn: yellow 52
g.add_vertex(249, 'Panchsheel Park') 
g.add_vertex(250, 'Chirag Delhi')
g.add_vertex(251, 'Greater Kailash')
g.add_vertex(252, 'Nehru Enclave')
#g.add_vertex(253, 'Kalkaji Mandir') #conn: violet 218
g.add_vertex(254, 'Okhla NSIC')
g.add_vertex(255, 'Sukhdev Vihar')
g.add_vertex(256, 'JAMIA MILLIA ISLAMIA')
g.add_vertex(257, 'Okhla Vihar')
g.add_vertex(258, 'Jasola Vihar Shaheen Bagh') 
g.add_vertex(259, 'Kalindi Kunj') 
g.add_vertex(260, 'Okhla Bird Sanctuary')
#g.add_vertex(261, 'Botanical Garden') #conn: blue 145


# AQUA LINE    10

#g.add_vertex(262, 'Noida Sector 51') #conn: blue 149
g.add_vertex(263, 'Noida Sector 50')
g.add_vertex(264, 'Noida Sector 76') 
g.add_vertex(265, 'Noida Sector 101')
g.add_vertex(266, 'Noida Sector 81') 
g.add_vertex(267, 'NSEZ Noida') 
g.add_vertex(268, 'Noida Sector 83') 
g.add_vertex(269, 'Noida Sector 137') 
g.add_vertex(270, 'Noida Sector 142')
g.add_vertex(271, 'Noida Sector 143')
g.add_vertex(272, 'Noida Sector 144') 
g.add_vertex(273, 'Noida Sector 145')
g.add_vertex(274, 'Noida Sector 146')
g.add_vertex(275, 'Noida Sector 147')
g.add_vertex(276, 'Noida Sector 148') 
g.add_vertex(277, 'Knowledge Park II')
g.add_vertex(278, 'Pari Chowk Greater Noida')
g.add_vertex(279, 'Alpha 1 Greater Noida')
g.add_vertex(280, 'Delta 1 Greater Noida') 
g.add_vertex(281, 'GNIDA Office')
g.add_vertex(282, 'Depot Greater Noida') 


# GRAY LINE   11


#g.add_vertex(283, 'Dwarka') #conn :blue 111
g.add_vertex(284, 'Nangli')
g.add_vertex(285, 'Najafgarh')

#RED LINE

g.add_edge(0,1,2)
g.add_edge(1,2,2)
g.add_edge(2,3,2)
g.add_edge(3,4,4)
g.add_edge(4,5,2)
g.add_edge(5,6,2)
g.add_edge(6,7,2)
g.add_edge(7,8,2)
g.add_edge(8,9,2)
g.add_edge(9,10,2) 
g.add_edge(10,11,3) 
g.add_edge(11,12,3)   #Conn: Pink
g.add_edge(12,13,2) 
g.add_edge(13,14,3) 
g.add_edge(14,15,3)  #Conn: Violet Conn: Yellow 
g.add_edge(15,16,2) 
g.add_edge(16,17,2) 
g.add_edge(17,18,2) 
g.add_edge(18,19,3) 
g.add_edge(19,20,3)  #Conn: Green
g.add_edge(20,21,2) 
g.add_edge(21,22,3) 
g.add_edge(22,23,3)  #Conn: Pink
g.add_edge(23,24,2) 
g.add_edge(24,25,2) 
g.add_edge(25,26,2) 
g.add_edge(26,27,2)  

#  YELLOW LINE

g.add_edge(28,29,2) 
g.add_edge(29,30,2) 
g.add_edge(30,31,2) 
g.add_edge(31,32,2) 
g.add_edge(32,33,3) 
g.add_edge(33,34,3)  # Conn: Pink
g.add_edge(34,35,2) 
g.add_edge(35,36,2) 
g.add_edge(36,37,2) 
g.add_edge(37,38,2) 
g.add_edge(38,14,3) 
g.add_edge(14,40,3)  #Conn: Violet, Red
g.add_edge(40,41,2) 
g.add_edge(41,42,3) 
g.add_edge(42,43,4)  #Conn: Orange
g.add_edge(43,44,3)  #Conn: Blue
g.add_edge(44,45,3) 
g.add_edge(45,46,3)  #Conn: Violet
g.add_edge(46,47,2) 
g.add_edge(47,48,2) 
g.add_edge(48,49,3) 
g.add_edge(49,50,3)  #Conn: Pink
g.add_edge(50,51,2) 
g.add_edge(51,52,3) 
g.add_edge(52,53,3)  #Conn: Magenta
g.add_edge(53,54,2) 
g.add_edge(54,55,2) 
g.add_edge(55,56,2) 
g.add_edge(56,57,2) 
g.add_edge(57,58,2) 
g.add_edge(58,59,2) 
g.add_edge(59,60,2) 
g.add_edge(60,61,3) 
g.add_edge(61,62,3)  #Conn: Rapid
g.add_edge(62,63,2) 
g.add_edge(63,64,2) 

# PINK LINE

g.add_edge(65,33,3) 
g.add_edge(33,67,3)  #Conn: Yellow
g.add_edge(67,22,3) 
g.add_edge(22,69,3)  #Conn: Red
g.add_edge(69,70,2) 
g.add_edge(70,71,2) 
g.add_edge(71,72,3) 
g.add_edge(72,73,3)  #Conn: Blue
g.add_edge(73,74,2) 
g.add_edge(74,75,2) 
g.add_edge(75,76,2) 
g.add_edge(76,77,2)  #Conn: Orange
g.add_edge(77,78,2) 
g.add_edge(78,79,2) 
g.add_edge(79,49,3) 
g.add_edge(49,81,3)  #Conn: Yellow
g.add_edge(81,82,3) 
g.add_edge(82,83,3)  #Conn: Violet
g.add_edge(83,84,2) 
g.add_edge(84,85,2) 
g.add_edge(85,86,3) 
g.add_edge(86,87,3)  #Conn: Blue
g.add_edge(87,88,2) 
g.add_edge(88,89,2) 
g.add_edge(89,90,2) 
g.add_edge(90,91,2)  
g.add_edge(91,92,3) 
g.add_edge(92,93,4)  #Conn: Blue
g.add_edge(93,94,3)  #Conn: Blue
g.add_edge(94,95,2) 
g.add_edge(95,96,2) 
g.add_edge(96,11,3) 
g.add_edge(11,98,3)  #Conn: Red
g.add_edge(98,99,2) 
g.add_edge(99,100,2) 
g.add_edge(100,101,2) 
g.add_edge(101,102,2) 


#BLUE LINE

g.add_edge(103,104,3) #conn : Orange
g.add_edge(104,105,2)
g.add_edge(105,106,2)
g.add_edge(106,107,2)
g.add_edge(107,108,2)
g.add_edge(108,109,2)
g.add_edge(109,110,2) 
g.add_edge(110,111,2) 
g.add_edge(111,112,2)  #conn : grey
g.add_edge(112,113,2) 
g.add_edge(113,114,2) 
g.add_edge(114,115,2)  
g.add_edge(115,116,3) 
g.add_edge(116,117,3) #conn: magenta
g.add_edge(117,118,2) 
g.add_edge(118,119,2) 
g.add_edge(119,120,2)  
g.add_edge(120,72,3) 
g.add_edge(72,122,3) #conn: pink
g.add_edge(122,124,2) 
#g.add_edge(122,124,2)
g.add_edge(124,125,3) 
g.add_edge(125,126,3) #conn : green
g.add_edge(126,127,2) 
g.add_edge(127,128,2)  
g.add_edge(128,129,2) 
g.add_edge(129,130,2) 
g.add_edge(130,131,2) 
g.add_edge(131,43,3) 
g.add_edge(43,133,3) #conn yellow
g.add_edge(133,134,3) 
g.add_edge(134,135,3) #conn : violet
g.add_edge(135,136,2) 
g.add_edge(136,137,3)  
g.add_edge(137,138,3) #conn :second branch of blue line
g.add_edge(138,86,3) 
g.add_edge(86,140,3) #conn :pink
g.add_edge(140,141,2) 
g.add_edge(141,142,2)
g.add_edge(142,143,2) 
g.add_edge(143,144,2) 
g.add_edge(144,145,3)
g.add_edge(145,146,3) #conn : magenta
g.add_edge(146,147,2)
g.add_edge(147,148,2)
g.add_edge(148,149,3)
g.add_edge(149,150,3) #conn: aqua
g.add_edge(150,151,2) 
g.add_edge(151,152,2)  
g.add_edge(152,153,2) 

#second branch of blue line

g.add_edge(137,155,3)  #conn: blue
g.add_edge(155,156,2) 
g.add_edge(156,157,3) 
g.add_edge(157,92,3) #conn: pink
g.add_edge(92,93,4) #conn :pink
g.add_edge(93,160,3)  
g.add_edge(160,161,2) 



#ORANGE LINE


g.add_edge(42,163,2) #conn : yellow
g.add_edge(163,164,6) 
g.add_edge(164,165,6) 
g.add_edge(165,166,3) 
g.add_edge(166,103,2) #conn : blue


#GREEN LINE


g.add_edge(19,169,4) #conn : red
g.add_edge(169,170,3) #conn : other branch of green line
g.add_edge(170,171,2) 
g.add_edge(171,172,2) 
g.add_edge(172,173,2) 
g.add_edge(173,174,2) 
g.add_edge(174,175,2) 
g.add_edge(175,176,2) 
g.add_edge(176,177,2)  
g.add_edge(177,178,2) 
g.add_edge(178,179,2) 
g.add_edge(179,180,2) 
g.add_edge(180,181,2) 
g.add_edge(181,182,2)
g.add_edge(182,183,2) 
g.add_edge(183,184,2) 
g.add_edge(184,185,2)
g.add_edge(185,186,2)
g.add_edge(186,187,2)
g.add_edge(187,188,2)

#other branch of green line

g.add_edge(169,190,3) 
g.add_edge(190,125,3) #conn : blue


#RAPID LINE

g.add_edge(192,193,2) 
g.add_edge(193,194,2) 
g.add_edge(194,195,2)  
g.add_edge(195,196,2) 
g.add_edge(196,61,3) 
g.add_edge(61,198,3) #Conn: Yellow 61
g.add_edge(198,199,2) 
g.add_edge(199,200,2)  
g.add_edge(200,201,2) 
g.add_edge(201,202,2) 

#VIOLET LINE


g.add_edge(14,204,3) #conn: wellow, red
g.add_edge(204,205,2) 
g.add_edge(205,206,2) 
g.add_edge(206,207,2)  
g.add_edge(207,134,3) 
g.add_edge(134,209,3) #conn : blue
g.add_edge(209,45,3) 
g.add_edge(45,211,3) #conn : yellow
g.add_edge(211,212,2) 
g.add_edge(212,213,2) 
g.add_edge(213,82,3) 
g.add_edge(82,215,3) #conn : pink
g.add_edge(215,216,2) 
g.add_edge(216,217,2)  
g.add_edge(217,218,3)
g.add_edge(218,219,3) #conn : magenta
g.add_edge(219,220,2) 
g.add_edge(220,221,2)
g.add_edge(221,222,2) 
g.add_edge(222,223,2) 
g.add_edge(223,224,2) 
g.add_edge(224,225,2) 
g.add_edge(225,226,2) 
g.add_edge(226,227,2)  
g.add_edge(227,228,2) 
g.add_edge(228,229,2) 
g.add_edge(229,230,2) 
g.add_edge(230,231,2) 
g.add_edge(231,232,2) 
g.add_edge(232,233,2) 
g.add_edge(233,234,2) 
g.add_edge(234,235,2) 
g.add_edge(235,236,2) 


#MAGENTA LINE


g.add_edge(116,238,3) #conn : blue
g.add_edge(238,239,2) 
g.add_edge(239,240,2) 
g.add_edge(240,241,2) 
g.add_edge(241,242,2) 
g.add_edge(242,243,2) 
g.add_edge(243,244,2) 
g.add_edge(244,245,2) 
g.add_edge(245,246,2) 
g.add_edge(246,247,2)  
g.add_edge(247,52,3) 
g.add_edge(52,249,3) #conn :yellow
g.add_edge(249,250,2) 
g.add_edge(250,251,2) 
g.add_edge(251,252,2) 
g.add_edge(252,218,3) 
g.add_edge(218,254,3) #conn : violet
g.add_edge(254,255,2) 
g.add_edge(255,256,2) 
g.add_edge(256,257,2)  
g.add_edge(257,258,2)
g.add_edge(258,259,2) 
g.add_edge(259,260,2) 
g.add_edge(260,145,3) #conn : blue


# AQUA LINE


g.add_edge(149,263,2)  #conn : blue
g.add_edge(263,264,2) 
g.add_edge(264,265,2) 
g.add_edge(265,266,2) 
g.add_edge(266,267,2)  
g.add_edge(267,268,2) 
g.add_edge(268,269,2) 
g.add_edge(269,270,2) 
g.add_edge(270,271,2) 
g.add_edge(271,272,2) 
g.add_edge(272,273,2) 
g.add_edge(273,274,2) 
g.add_edge(274,275,2) 
g.add_edge(275,276,2) 
g.add_edge(276,277,2)  
g.add_edge(277,278,2)
g.add_edge(278,279,2) 
g.add_edge(279,280,2) 
g.add_edge(280,281,2) 
g.add_edge(281,282,2) 


#GRAY LINE


g.add_edge(111,284,3) #conn : blue
g.add_edge(284,285,2) 
