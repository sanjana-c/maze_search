# search.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created by Kelvin Ma (kelvinm2@illinois.edu) on 01/24/2021

"""
This is the main entry point for MP1. You should only modify code
within this file -- the unrevised staff files will be used for all other
files and classes when code is run, so be careful to not modify anything else.
"""
# Search should return the path.
# The path should be a list of tuples in the form (row, col) that correspond
# to the positions of the path taken by your search algorithm.
# maze is a Maze object based on the maze from the file specified by input filename
# searchMethod is the search method specified by --method flag (bfs,dfs,astar,astar_multi,fast)

import heapq

def bfs(maze):

    """
    Runs BFS for part 1 of the assignment.
    

    @param maze: The maze to execute the search on.

    @return path: a list of tuples containing the coordinates of each state in the computed path
    """
    goal = maze.waypoints[0]
    
    
    visited = set()
    queue = []
    queue.append([maze.start])
    #visited.add(maze.start) #??

    while queue:
        path = queue.pop(0)
        currPoint = path[-1]
        row, col = currPoint
        if currPoint not in visited:
            visited.add(currPoint)
        else:
            continue
        if currPoint == goal:
            return path
        neighbors = maze.neighbors(row, col)
        
        for n in neighbors:
            r, c = n
            if n not in visited and maze.navigable(r, c):
                visited.add(currPoint)
                queue.append(path + [n])
            
    
    
    return []


def astar_single(maze):
    """
    Runs A star for part 2 of the assignment.

    @param maze: The maze to execute the search on.

    @return path: a list of tuples containing the coordinates of each state in the computed path
    """

    goal = maze.waypoints[0]
    final_row, final_col = goal

    queue = []
    heapq.heappush(queue, (0, 0, [maze.start]))
    
    visited = {}
    
    while queue:
        node = heapq.heappop(queue)
        f, g, path = node
        
        row, col =  path[-1]
        neighbors = maze.neighbors(row, col)
        if (row, col) in visited.keys():
            if visited[(row,col)] < f:
                continue
            else:
                visited[(row, col)] = f
                
        else:
            visited[(row, col)] = f

        if (row, col) == goal:
            return path
       
        for n in neighbors:
            
            r, c = n
            if n not in visited.keys():
                new_path = path + [n]
                g += 1
                h = abs(r - final_row) + abs(c - final_col)
                f = g + h
                visited[(r,c)] = f
                heapq.heappush(queue, (f, g, new_path))   
            else :
                if visited[(r,c)] > f:
                    
                    visited[(r, c)] = f
                    heapq.heappush(queue, (f, g, new_path))
                else:
                    continue
    return []

