# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 13:57:10 2021

@author: srpdo

poisson distrubution
"""

import numpy as np
import matplotlib.pyplot as plt


def poisson(n_observed,n_repetation):
    #a function to calculate the poisson distrubition of given array 
    
    expected = []                   #will hold the expected values according to poisson distrubition
    total_obv = 0
    total_rep= 0
    
    #for loop to calculate the weighted average of the given data set
    
    for i in range(len(n_observed)):
        total_obv += n_observed[i]*n_repetation[i]
        total_rep += n_observed[i]
    mu = total_obv/total_rep
    pois_exp = np.exp(-mu)
    
    #a for loop to finally calculate expectation values for each data point, and fills the final array
    
    for i in range(len(n_Observed)):
        x=n_repetation[i]
        pois_coef = (mu**x)/(np.math.factorial(x))
        expected.append(total_rep*pois_exp*pois_coef)
    
        
    #function returns a list filled with the expected values for data points
    return expected
        
    
n_Events = [i for i in range(10) ]                          #given data

n_Observed = [1043, 860, 307, 78, 15, 3, 0, 0, 0, 1]        #given data



poisson_fit = poisson(n_Observed,n_Events)                  #using the poisson dist. function defined above



figure,axis = plt.subplots(1,2)                             #creates a canvas to plot 2 graphs in 1 row

axis[0].bar(n_Events,n_Observed,label="Data")               #plots a bar graph with the given data
axis[0].plot(poisson_fit,"r*",label="Expected")             #plots the poission distrubition on top of the data
axis[0].legend()                                            #shows legend for the first graph
axis[0].set_title("Experimental Data")
axis[0].set_xlabel("Observation Frequency")
axis[0].set_ylabel("Number of events")


axis[1].bar(n_Events, n_Observed,label="Data")              #plots the second graph
axis[1].set_yscale("log")                                   #setting a logarithmic scale in y axis of the second plot 
axis[1].plot(poisson_fit,"g*",label="Expected")             #plotting the poisson dist. for the second graph
axis[1].legend()                                            #shows legend for the second graph

axis[1].set_title("Log Experimental Data")
axis[1].set_xlabel("Observation Frequency")


plt.show()                                                  #shows the graphs

