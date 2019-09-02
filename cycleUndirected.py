#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 10:59:17 2019

@author: amogh
"""

T = int(input()) 
for t in range(T): 
    
    N = int(input()) 
    g = dict()
        
    for i in range (N): 
        x, y = map(int, input().split()) 
        g.setdefault(x-1, list()).append(y-1) 
        g.setdefault(y-1, list()).append(x-1)
        
    #DFS for cycle detection  
    
    visited = [False]*len(g) 
    cycle = [False]*len(g)
    depth = [None]*len(g) 
    stack = [] 
    N = 0
            
    stack.append(0) #Starting vertex 
    depth[0] = 1 
    visited[0] = True 
    detected = False
            
    while stack and not detected: 
        s = stack.pop() 
        for i in g[s]:
          
            if depth[i]!=None: 
                if depth[i] <= depth[s]-2:
                    cycle[s] = True
                    detected = True
                    N = depth[s]-depth[i]
                    break
                    
            if visited[i] == False: 
                depth[i] = depth[s] + 1
                visited[i] = True 
                stack.append(s)
                stack.append(i) 
                break
                    
    for num in range (0, N): 
        s = stack.pop()
        cycle[s] = True
    
    #list cycle contains vertices belonging to the cycle
    #BFS for shortest distance 
    
    queue = [] 
    visited = [False]*len(g) 
    dist = [0]*len(g)
        
    for i in range (len(cycle)): 
        if cycle[i] == True: 
            break
        
    queue.append(i)
    visited[i] = True
        
    while queue:
        s = queue.pop(0)
            
        for i in g[s]: 
            if visited[i] == False: 
                queue.append(i)
                visited[i] = True 
                    
                if cycle[i] == False:
                    dist[i] = dist[s]+1
    
    print("Case #", t+1, ":", sep='', end=' ')
    for i in dist: 
        print(i, " ", sep='', end='') 
    print()

"""
class Graph: 
    
    def __init__(self): 
        self.graph = dict() 
        self.cycle = list() 
        
    def addEdge(self,u,v): 
        self.graph.setdefault(u, list()).append(v) 
        self.graph.setdefault(v, list()).append(u) 
        
    def show(self):
        print(self.graph) 
        
    def BFS(self): 
        queue = [] 
        visited = [False]*len(self.graph) 
        dist = [0]*len(self.graph)
        
        for i in range (len(self.cycle)): 
            if self.cycle[i] == True: 
                break
        
        queue.append(i)
        visited[i] = True
        
        while queue:
            s = queue.pop(0)
            
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i)
                    visited[i] = True 
                    
                    if self.cycle[i] == False:
                        dist[i] = dist[s]+1
        return dist          
        
        
    def DFS(self): 
        visited = [False]*len(self.graph) 
        self.cycle = [False]*len(self.graph)
        depth = [None]*len(self.graph) 
        stack = [] 
        N = 0
        
        stack.append(0) #Starting vertex 
        depth[0] = 1 
        visited[0] = True 
        detected = False
        
        while stack and not detected: 
            s = stack.pop() 
            for i in self.graph[s]:
                
                if depth[i]!=None: 
                    if depth[i] <= depth[s]-2:
                        self.cycle[s] = True
                        detected = True
                        N = depth[s]-depth[i]
                        break
                
                if visited[i] == False: 
                    depth[i] = depth[s] + 1
                    visited[i] = True 
                    print("Visited", i, "Depth", depth[i]) 
                    stack.append(s)
                    stack.append(i) 
                    break
                
        for num in range (0, N): 
                s = stack.pop()
                self.cycle[s] = True
                
        print(self.cycle)
"""