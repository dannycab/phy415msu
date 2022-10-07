#!/usr/bin/env python
# coding: utf-8

# # 27 Sept 22 - Activity: Normal Modes
# 
# As we begin to work with multi-particle systems, we begin to open the number of degrees of freedom of the system. We increase the complexity of it and the challenge of modeling it. We will increasingly need tools that help us take less tractable issues and make them palatable. One such tool that forms the basis of many others is **Normal Modes**.
# 
# Normal modes are ways of breaking up our understanding of a system into discrete (potentially infinite and hopefully vanishingly small) pieces. This lets us get at the big picture of the system and characterize how much we are neglecting. The concept of normal modes underlies much of the analysis done in quantum mechanics, field theory, fluid mechanics, and signal processing. In fact, numerical routines often make use of forms of these modes to do economize calculations -- *especially when we move beyond a few hundred bodies in the system*. This stuff is part and parcel of most research in physics. For example, how we understand the [Cosmic Background Radiation](https://en.wikipedia.org/wiki/Cosmic_background_radiation) relies on a [normal mode like analysis](https://www.quantamagazine.org/how-ancient-light-reveals-the-universes-contents-20200128/).
# 

# ## Guided Lecture: Canonical Coupled Oscillators
# 
# 
# There is still plenty of room for pencil and paper. We will explore this numerically later. 
# 
# We will start with a form of guided lecture and build the understanding of these methods together. Then you will apply what you learned to a new system.
# 
# Let's assume you have a chain of two mass connected by springs (all the same $k$) as below.
# 
# <img src='https://www.entropy.energy/static/resources/coupled-oscillators/two-coupled-gliders-diagram.png' alt='Coupled Oscillator set up. Two oscillators connected by three springs in a horizontal line.' width=800px/>
# 
# ### Method 1: Assume the solution
# 
# **&#9989; Do this** 
# 
# 1. Displace the left mass by $x_1$ and the right mass by $x_2$ at $t=0$. Write down the pair of second order linear differential equations that describes the motion of this system.
# 2. Assume the solutions to both will be simply oscillatory (e.g., sinusoidal). Plug the general solutions into your differential equation and find the particular solutions. Can you determine the oscillatory behavior of each solution?
# 3. Pick numbers for your unknowns (e.g., $x_1$, $x_2$, $k$) and plot your position vs. time solutions. Does this picture help determine the motion? Is it purely sinusoidal?
# 

# In[1]:


## Your code here


# ### Method 2: Find the normal modes
# 
# **&#9989; Do this** 
# 
# 1. Displace the left mass by $x_1$ and the right mass by $x_2$ at $t=0$. Again, write down the pair of second order linear differential equations that describes the motion of this system.
# 2. Rework the differential equation into a matrix description: $\ddot{\mathbf{x}} = \pmb{A} \mathbf{x}$. Why can you do this? When can you not do this? Or rather what about the differential equation lets us do this?
# 3. Find the determinant of the coefficient matrix $\pmb{A}$, and use that to determine the oscillation frequencies.
# 4. Plot the normal mode solutions (remember we assume sinusoidal normal modes); there should be two.
# 
# 
# 

# In[2]:


## your code here


# ## Apply: 
# 
# Consider two vertical pendulums of length $l$ connected via their masses $M$ by a weak spring $k$. By weak, we mean that the spring constant is small. See below for a canonical setup:
# 
# <img src="http://www.maths.surrey.ac.uk/explore/michaelspages/coupled/coupled_diag.jpg" />
# 
# **&#9989; Do this** 
# 
# 1. In this limit, write down the pair of second order linear differential equations for the horizontal motion of each pendulum bob around its equilibrium.
# 2. Find and describe the normal modes. Use plots of your choosing to explain what you found.
# 3. Can you build up particular solutions from sums and differences of normal modes? 

# In[3]:


## your code here

