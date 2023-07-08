from queue import PriorityQueue

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic[start], start))
    
    while not pq.empty():
        h,node = pq.get()
        
        if node == goal:
            print("Goal reached:", node)
            return
        
        if node not in visited:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    pq.put((heuristic[neighbor], neighbor))
            
            print("Visiting node:", node)
            visited.add(node)
    
    print("Goal not found!")

# Example graph representation using adjacency list
graph = {
    'S':[('A'),('B')],
    'A': [('C'), ('D')],
    'B': [('E'), ('F')],
    'C': [],
    'D': [],
    'E': [('H')],
    'F': [('I'), ('G')],
    'H':[],
    'I':[],
    'G':[],
}

start_node = 'S'
goal_node = 'G'

#Heuristic values from curr node -> goal node
heuristic_values = {
    'S': 13,
    'A': 12,
    'B': 4,
    'C': 7,
    'D': 3,
    'E': 8,
    'F': 2,
    'H': 4,
    'I': 9,
    'G': 0,
}

best_first_search(graph, start_node, goal_node, heuristic_values)