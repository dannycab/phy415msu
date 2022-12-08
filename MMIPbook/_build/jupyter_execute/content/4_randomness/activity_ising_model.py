#!/usr/bin/env python
# coding: utf-8

# # 8 Dec 2022 - The Ising Model
# 
# $$E = -J\left(\vec{S}_i\cdot\vec{S}_j\right)$$

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import random as random


# In[2]:


cellLength = 20
simulationSteps = 100000
couplingConstant = 1.0 ## J
temperature = 2.0

def calculateEnergy(spinArray):
    '''Calculate all the pairwise energy interactions and sum them up
    Do rows and columns separately and add them up.'''
    
    rowNeighborInteractionEnergy = np.sum(spinArray[0:cellLength-1,:]*spinArray[1:cellLength,:])
    columnNeighborInteractionEnergy = np.sum(spinArray[:,0:cellLength-1]*spinArray[:,1:cellLength])
    
    totalInteractionEnergy = rowNeighborInteractionEnergy+columnNeighborInteractionEnergy
    
    return -couplingConstant*totalInteractionEnergyamek

## Create an empty square array
spinArray = np.empty([cellLength,cellLength], int)

## Populate it with random spins
for row in range(cellLength):
    for column in range(cellLength):
        if random.random()<0.5:
            spinArray[row,column] = +1
        else:
            spinArray[row,column] = -1

# Calculate the initial energy and magnetization        
energyAtStep = calculateEnergy(spinArray)
magnetizationAtStep = np.sum(spinArray)

## Show the spin array 
## Black is spin up and white is spin down
plt.figure(figsize=(8,8))
c = plt.pcolor(spinArray, cmap='Greys')
plt.axis('square')


# In[31]:


## Hold onto the values of the magnetization 
## for each step in the simulation
magnetizationArray = np.zeros(simulationSteps)

## Monte Carlo Loop
for step in range(simulationSteps):
    
    ## Store the magnetization at this step
    
    ## Store the energy before swapping the spin randomly
    
    ## Select a spin from the cell
    
    ## Flip the spin of that one site
    
    ## Calculate the energy after that change
    ## Calculate the change in energy 
    
    
    ## If the change resulted in an increase in the total energy,
    ## evaluate whether to accept the value or not
    if deltaE > 0.0:
        
        probabilityOfFlip = np.exp(-deltaE/temperature)
        
        ## If the the random value is lower than the probability,
        ## reverse the change to the spin, and recalculate the energy
        if random.random()>probabilityOfFlip:
            
            continue
        
    ## Sum up the magnetization at that step    
    


# In[ ]:




