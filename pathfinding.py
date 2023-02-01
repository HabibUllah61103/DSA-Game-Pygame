from collections import deque

#Data structure for pathfinding

class PathFinding:
    '''Path finding class
    Get graph and path'''
    def __init__(self, game):
        self.game = game
        self.map = game.map.mini_map
        self.ways = [-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, -1], [1, 1], [-1, 1]
        self.graph = {}
        self.get_graph()

    def get_path(self, start, goal):
        '''Get path from start to goal
        Return path'''

        self.visited = self.bfs(start, goal, self.graph)
        path = [goal]
        step = self.visited.get(goal, start)

        while step and step != start:
            path.append(step)
            step = self.visited[step]
        return path[-1]

    def bfs(self, start, goal, graph):
        '''Breadth-first search
        Return visited'''

        queue = deque([start])  # Queue for BFS
        visited = {start: None} # Visited nodes

        while queue:    # While queue is not empty
            cur_node = queue.popleft()  # Get current node
            if cur_node == goal:    # If current node is goal,
                break   
            next_nodes = graph[cur_node]   # Get next nodes

            for next_node in next_nodes:    # For each next node
                if next_node not in visited and next_node not in self.game.object_handler.npc_positions:    # If next node is not visited and not in npc positions
                    queue.append(next_node) # Append next node to queue
                    visited[next_node] = cur_node   # Set next node as visited
        return visited      # Return visited

    def get_next_nodes(self, x, y):
        '''Get next nodes
        Return next nodes'''

        return [(x + dx, y + dy) for dx, dy in self.ways if (x + dx, y + dy) not in self.game.map.world_map]

    def get_graph(self):
        '''Get graph'''
        for y, row in enumerate(self.map):  # For each row
            for x, col in enumerate(row):   # For each column
                if not col: # If column is not wall
                    self.graph[(x, y)] = self.graph.get((x, y), []) + self.get_next_nodes(x, y) # Get next nodes