#!/usr/bin/env python
# coding: utf-8

# # 29 Sept 22 - Activity: Lagrangian Dynamics
# 
# Motivation to be completed later...
# 
# Here you will practice using the Lagrangian for increasingly complex systems. We start with the SHO and move forward from there.
# 
# Using Lagrangian dnymaics can feel like magic. In fact, this is video of me from 2002 when I learned to use this approach:
# 
# <img src="https://c.tenor.com/zcs5gYi4sSMAAAAC/mindblown-omg.gif" alt="mind blown cat gif" width=400px/>
# 
# But we will step through the levels of complexity with these examples to make sure we all understand how to make use of them.
# 
# <img src="https://i.imgflip.com/6v4j4k.jpg" alt="Lagrange meme" width=400px/>

# ## Getting Started
# 
# ### Simple Harmonic Oscillator
# 
# **&#9989; Do this** 
# 
# 1. Starting with the 1d energy equations (for $x$ and $\dot{x}$) for an SHO; derive the equations of motion. Did you get the sign right?
# 
# ## #Canonical Coupled Oscillators
# 
# Let's assume you have a chain of two mass connected by springs (all the same $k$) as below.
# 
# <img src='https://www.entropy.energy/static/resources/coupled-oscillators/two-coupled-gliders-diagram.png' alt='Coupled Oscillator set up. Two oscillators connected by three springs in a horizontal line.' width=800px/>
# 
# **&#9989; Do this** 
# 
# 1. Write down the energy equations for this system (using $x_1$ and $x_2$ for coordinates)
# 2. Write the Lagrangian and derive the two equations of motion.
# 3. Do all the signs makes sense to you?
# 
# 

# ## Choose your coordinates
# 
# ### Coupled Pendulums
# 
# Consider two vertical pendulums of length $l$ connected via their masses $M$ by a weak spring $k$. By weak, we mean that the spring constant is small. See below for a canonical setup:
# 
# <img src="http://www.maths.surrey.ac.uk/explore/michaelspages/coupled/coupled_diag.jpg" />
# 
# **&#9989; Do this** 
# 
# 1. Write down the energy equations for this system (think about your choices of coordinates)
# 2. Write the Lagrangian and derive the two equations of motion (we want to know what is happening with both bobs)
# 3. Compare your work to another group. Did they choose the same coordinates?
# 

# ## Adding Constraint Forces
# 
# ![Rubric](../../assets/images/cylindrical_cone_mass.jpg)
# 
# 
# Consider a particle of mass $m$ constrained to move on the interior surface of a upside down smooth ice cream cone (aligned with the vertical axis) with half-angle $\alpha$ subject to a gravitational force downward, so that the cone axis and gravity are aligned.
# 
# 1. Using cylindrical coordinates (why?), write down the equation of constraint. Think about where the mass must be if it's stuck on a cone.
# 2. Write the energy contributions in cylindrical coordinates. (This is where you put in the constraint!)
# 3. Form the Lagrangian and find the equations of motion (there are two!)

# In[1]:


## your code here


# In[ ]:




