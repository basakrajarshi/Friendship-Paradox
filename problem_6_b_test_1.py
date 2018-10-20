# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 22:07:04 2018

@author: rajar
"""

from numpy import genfromtxt

edgelist = {}
total_squared_edges = 0 
with open('UPenn7.txt') as f:
    content = f.readlines()

total_degrees = len(content) #2m
my_data = genfromtxt('American75.txt', delimiter='\t')
total_vertices = len(set(my_data[:, 0])) #n
mean_degree = total_degrees/total_vertices

# Create dictionary to store the number of edges for each vertex
for i in my_data[:,0]:
    if (i not in edgelist):
        edgelist[i] = 1
    else:
        edgelist[i] += 1
        
# Find the sum of the squared degree of each vertex
for i in edgelist:
    total_squared_edges += edgelist[i]*edgelist[i]

mean_squared_degree = total_squared_edges/total_vertices
mean_neighbour_degree = mean_squared_degree/(mean_degree)
ratio = mean_neighbour_degree/mean_degree

print(ratio, mean_degree)




