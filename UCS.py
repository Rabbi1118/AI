# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:04:28 2021

@author: Rabbi
"""

import math
def UCS(adjList, start, goal):

    frontier = [start]
    exploredSet = []
    parent = {start:''}

    #*************************
    pathCost = {start:0}
    #*************************

    print("Searching Sequence = ",end='')
    while True:
        if len(frontier)==0:
            print("No solution")
            return

        #**************************************
        #Find the minimum node from the frontier
        node=''
        minValue = math.inf
        for item in frontier:
            if pathCost[item]<minValue:
                minValue=pathCost[item]
                node=item
        frontier.remove(node)    #Remove the minimum node from the frontier
        #**************************************

        print(node,end ='-->')

        if node == goal:
            print()
            print("Solution Sequence= ",end='')
            n = goal
            lst = []
            while n!='':
                lst.append(n)
                n=parent[n]

            while len(lst)!=0:
                print(lst.pop(),end='-->')

            print("\nPath Cost = ",pathCost[goal])
            return

        exploredSet.append(node)

#**************************************     
        for adNode, weight in adjList[node]:
            if adNode not in frontier and adNode not in exploredSet:
                frontier.append(adNode)
                parent[adNode] = node
                pathCost[adNode] = pathCost[node]+weight
            elif adNode in frontier:
                if pathCost[adNode]>pathCost[node]+weight:
                    parent[adNode] = node
                    pathCost[adNode] = pathCost[node]+weight
 
#************************************** 
 
 
 
 
adjacencyList = {'A':[('B',3),('J',4),('G',1)],
                 'B':[('A',3),('D',10)],
                 'C':[('H',3)],
                 'D':[('B',10),('J',3),('H',11)],
                 'E':[('G',14),('F',2), ('I',1)],
                 'F':[('E',2),('G',8),('H',4),('I',2)],
                 'G':[('A',1),('J',6),('F',8),('E',14)],
                 'H':[('C',3),('F',4),('I',6),('D',11)],
                 'I':[('E',1),('F',2),('H',6)],
                 'J':[('A',4),('D',3),('G',6)]}
 

UCS(adjacencyList, 'A','C')