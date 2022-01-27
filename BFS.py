# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 22:44:38 2021

@author: Rabbi
"""

def DFS(adjList, start, goal):
    frontier = [start]
    exploredSet = []
    parent = {start: ''}
    
    
    print("Searching Sequence: ", end='');
    while True:
        if len(frontier) == 0:
            print("No Solution")
            return
        
        #node = frontier.pop()
        node = frontier.pop(0)   #BFS
        print(node, end="-->")
        
        if node == goal:
            print()
            print("Goal Found")
            print("Solution Sequence: ", end='')
            n = goal
            lst = []
            while n!='':
                lst.append(n)
                n = parent[n]
                
            while len(lst)!=0:
                print(lst.pop(),end="-->")
                
            return
        
        exploredSet.append(node)
        
        for adjNode in adjList[node]:
            if adjNode not in frontier and adjNode not in exploredSet:
                frontier.append(adjNode)
                parent[adjNode] = node

 

    

 


adjacencyList = {'A': ['B', 'C'],
                 'B': ['A', 'C', 'D'],
                 'C': ['A','B','D','E'],
                 'D': ['B','C','E','F'],
                 'E': ['C','D'],
                 'F': ['D']}

 


DFS(adjacencyList, 'A', 'F')

 


#print(adjacencyList['E'])