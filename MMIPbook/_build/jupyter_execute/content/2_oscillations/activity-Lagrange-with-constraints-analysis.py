#!/usr/bin/env python
# coding: utf-8

# # Activity: Analyzing Lagrangian Dynamics with Constraints
# 
# One of the strengths of Lagrangian dynamics is that you do not have to have a mathematical description of the forces for all space and time. We can see that in this upside-down ice cream cone problem. How would you write the force of the cone for all space and time?
# 
# *Answer:* :shrugs:
# 
# ![Rubric](../../assets/images/cylindrical_cone_mass.jpg)
# 
# ## Last time
# 
# We used Lagrangian Analysis to produce the following differential equations:
# 
# $$m\ddot{r} = (mr^2\dot{\theta}-mg\cot\alpha)\cos^2\alpha$$
# 
# $$\dfrac{d}{dt}\left(mr^2\dot{\theta}\right) = 0$$
# 
# We made a note that the second one tells about conservation of angular momentum in the $z$-direction.
# 

# Let's write this a bit different, so we can integrate the situation:
# 
# $$m\ddot{r} = (mr^2\dot{\theta}-mg\cot\alpha)\cos^2\alpha$$
# 
# $$2mr\dot{r}\dot{\theta}+mr^2\ddot{\theta} = 0$$
# 
# Now we need to write this as a set of first order differential equations. Let $v=\dot{r}$ and $\omega=\dot{\theta}$. Then we get the following four equations

# $$\dot{v} = \left(r^2\omega-g\cot\alpha\right)\cos^2\alpha$$
# 
# $$\dot{r} = v$$
# 
# $$\dot{\omega} = -2\dfrac{v\omega}{r}$$
# 
# $$\dot{\theta} = \omega$$

# ## Start your analysis
# 
# Now we have four 1st order, coupled, nonlinear differential equations that describe the motion of this bead. We are going to solve for $r(t)$ and $\theta(t)$ for a given choice of $\alpha$. This will produce a solution for $z(t) = \dfrac{r(t)}{\tan\alpha}$. We can investigate phase space, but you will have to look at slices of it and try to make sense of different projections. Let's start with the doing the following three tasks:
# 
# We will construct phase space diagrams for $r$ and $\theta$.
# 
# 1. You will have to use numpy.meshgrid for four variables. If you put in four variables, then you will get out ordered groups of the four variables.
# 2. You need to define a function that returns the four changes of the four variables (remember we had to take the ordered pairs and then compute the arrows)
# 3. Plot a 2d slice (e.g., $r$ vs $v$) 

# In[1]:


## Your code here


# ## Numerically Integrate our EOM
# 
# Ok, now that you have looked at the phase space as discuss possible motion that could occur. Let's pick some initial conditions and build a numerical model. 
# 
# Using the integrator of your choice, numerically integrate and plot (in 3d) the motion of the bead for the following conditions:
# 
# 1. Bead starts from rest and is let go
# 2. Bead starts at a given height and is given a low speed (less than needed to orbit)
# 3. Bead starts at a given height and is given a low speed (more than needed to orbit)
# 4. Can you find a flat horizontal orbit?

# In[2]:


## your code here

