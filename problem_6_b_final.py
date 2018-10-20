# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 19:37:21 2018

@author: rajar
"""

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import glob

def getgraphparameters(filename):
    mean_degree = 0
    total_edges = 0
    total_vertices = 0
    total_squared_degree = 0
    mean_squared_degree = 0
    mean_neighbour_degree = 0
    ratio = 0
    
    graph = nx.read_edgelist(filename, nodetype=int, data=(('weight',float),))
    
    total_edges = len(graph.edges())
    total_vertices = len(graph.nodes())
    mean_degree = 2*(total_edges)/total_vertices
    
    for i in graph.nodes():
        total_squared_degree += len(graph.edges(i))**2

    mean_squared_degree = total_squared_degree/total_vertices
    mean_neighbour_degree = mean_squared_degree/mean_degree
    ratio = mean_neighbour_degree/mean_degree
    #print(ratio)
    return (mean_degree, ratio, mean_neighbour_degree)

parameters = {}
for filename in glob.glob('*.txt'):
    print(filename)
    ra, md, mnd = getgraphparameters(filename)
    print (ra, md, mnd)
    parameters[filename] = (ra, md, mnd)
    
print(parameters)   

x = np.zeros((95))
y = np.zeros((95))
ind = 0
for j in parameters:
    temp=(parameters[j])
    
    if j=='Reed98.txt':
        xreed98 = temp[0]
        yreed98 = temp[1]
    elif j=='Bucknell39.txt':
        xbuck = temp[0]
        ybuck = temp[1]
    elif j=='Mississippi66.txt':
        xmiss = temp[0]
        ymiss = temp[1]
    elif j=='Virginia63.txt':
        xvirg = temp[0]
        yvirg = temp[1]
    elif j=='Berkeley13.txt':
        xberk = temp[0]
        yberk = temp[1]
    else:
        x[ind] = temp[0]
        y[ind] = temp[1]
        ind = ind+1
        
plt.scatter(xreed98,yreed98, alpha = 1.0, color = 'r',marker = '^')
plt.scatter(xbuck,ybuck, alpha = 1.0, color = 'm', marker = '*')
plt.scatter(xmiss,ymiss, alpha = 1.0, color = 'y', marker = 's')
plt.scatter(xvirg,yvirg, alpha = 1.0, color = 'g', marker = 'X')
plt.scatter(xberk,yberk, alpha = 1.0, color = 'b', marker = 'v')
plt.scatter(x,y, alpha=0.5, color = 'c')

plt.legend(( 'Reed', 'Bucknell', 'Mississippi', 'Virginia',
            'Berkeley'))

xx = np.linspace(35, 125, num=100)
yy = np.ones(np.size(xx))
plt.plot(xx,yy,linestyle='-.', color='k', linewidth=3)
plt.xlabel('<k_u>')
plt.ylabel('<k_v>/<k_u>')
plt.ylim((0.9,3.1))
plt.savefig('k_v_k_u-vs-k_u-plot.png', dpi = 300)
plt.show()    
    
    
    
    