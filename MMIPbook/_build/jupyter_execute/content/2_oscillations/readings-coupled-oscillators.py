#!/usr/bin/env python
# coding: utf-8

# Book Reading: Crawford, Waves, Secs 1.4-1.5
# 
# # Notes: Coupled Oscillators
# 
# Single particle dynamics like the SHO and other singular point particle motion (e.g., basic kinematics, charges in fields modeled without interactions) are helpful in building our intutiion of how physics _should_ work. We can track the position, velocity, and other dynamical quantities for these singular particles. We can determine how the act on and interact with their surroundings. We can find points of stasis (stable and unstable points); we can find different families of solutions (orbits vs runaway behavior); we can predict the motion of those particles with numerical routines.
# 
# But what happens when we introduce a second particle? And we let it interact with the first particle. We have substantially opened the degrees of freedom (a way to characterize the complexity of our system) that our system has. We will see how these systems become expanded and how their dynamics becomes richer and more interesting.
# 
# The canonical complication is the coupled oscillators, which will form the basis of our initial study, much like the SHO formed our initial work for dynamical models using ODEs. The setup appears below:
# 
# <img src='https://www.entropy.energy/static/resources/coupled-oscillators/two-coupled-gliders-diagram.png' alt='Coupled Oscillator set up. Two oscillators connected by three springs in a horizontal line.' width=800px/>
# 
# We will set up this problem below, but our analysis will proceed in class. To motivate our study of coupled oscillations, watch this excellent video (20 minutes) on the phenomenon on [synchronization](https://physicstoday.scitation.org/doi/10.1063/1.1554136).

# In[1]:


from IPython.display import YouTubeVideo
YouTubeVideo("t-_VPRCtiUg", 800, 600)


# ## Synchronization
# 
# Nature exhibits many different kinds of behaviors that we have organized into different concepts (i.e., random, chaotic, deterministic, synchronized). THese behaviors have interesting properties and allow us to bring different and new forms of mathematics and computing to the work; this includes new areas like machine-learning based physics models](). As we move from a single object models to multiple objects models, we begin to explore these different conceptual behaviors. [Synchronization](https://www.quantamagazine.org/physicists-discover-exotic-patterns-of-synchronization-20190404/) is one that is common and natural to consider in the context of oscillations as you saw from the above video. [Fireflies](https://www.youtube.com/watch?v=ZGvtnE1Wy6U), [patterns in the operation of a heart](https://www.youtube.com/watch?v=2LPboySOSvo), and [coupled metronomes](https://www.youtube.com/watch?v=5v5eBf2KwF8) all exhibit this synchronized behavior. But, how is that possible? What physics is going on here? And how can it lead in and out of synchronization like this pendulum setup below?
# 

# In[2]:


from IPython.display import YouTubeVideo
YouTubeVideo("yVkdfJ9PkRQ", 800, 600)


# ```{admonition} Huygen's Clocks
# Much of this early understanding of synchronization we owe to the Dutch mathematician, [Christiann Huygens](https://en.wikipedia.org/wiki/Christiaan_Huygens), who spent much of his work trying to understand periodic motion. In this work, he observed the oscillation of two pendulum clocks that would eventually oscillate in precisely opposite swings. A great writeup of this history and its implications is [here](https://www.quantamagazine.org/physicists-discover-exotic-patterns-of-synchronization-20190404/). This phenomenon was explored experimentally and theoretically by three physicists at Georgia Tech, Matt Bennet, Mike Schatz (my Phd Advisor!), and Kurt Wiesenfeld. Their paper was written in collaboration with, history and language professor emerita, Heidi Rockwood. It's a [fun read](http://engineering.nyu.edu/mechatronics/Control_Lab/bck/VKapila/Chaotic%20Ref/Hujgens.pdf).
# 
# We know use this phenomenon to [entrain oscillators](https://en.wikipedia.org/wiki/Injection_locking#Entrainment); this kind of mode locking is really important to science -- especially ultra-fast science. Physicists like [Dr. Jennifer Ogilive at the University of Michigan](https://www.ogilviegroup.org/) use this phenomenon to image biological materials that undergo very fast transitions.
# ```

# ## Coupled Oscillations
# 
# The key to why these phenomena are possible is the increase in the number of **Degrees of Freedom**. You can think of this as the [ways in which the system can move](https://en.wikipedia.org/wiki/Degrees_of_freedom_(mechanics)) -- really we should try to think of it as the [additional variables in phase space](https://en.wikipedia.org/wiki/Degrees_of_freedom_(physics_and_chemistry)) that become available by adding more particles and interactions. We will start with the canonical longitudinal oscillations of two coupled spring oscillators.
# 
# <img src='https://www.entropy.energy/static/resources/coupled-oscillators/two-coupled-gliders-diagram.png' alt='Coupled Oscillator set up. Two oscillators connected by three springs in a horizontal line.' width=800px/>
# 
# Our analysis will proceed with an investigation of [normal modes](https://en.wikipedia.org/wiki/Normal_mode), which is a powerful tool that lets us not only analyze systems with many degrees of freedom; it can help us conceptually think about building up solutions for continuous systems that have infinite degrees of freedom (i.e., a rope or a water wave).

# We start by writing the differential equations that describe the motion of the system, noting that the length measures are critical for establishing the right differential equation:
# 
# Left mass:
# $$m \ddot{x}_{1} = -k x_1 + k'(x_2-x_1)$$
# 
# Right mass:
# $$m \ddot{x}_{2} = - k'(x_2-x_1)-kx_2$$
# 
# We can write these in the following way:
# $$\ddot{x}_{1} = -\dfrac{k}{m} x_1 + \dfrac{k'}{m}(x_2-x_1)$$
# $$\ddot{x}_{2} = - \dfrac{k'}{m}(x_2-x_1)-\dfrac{k}{m}x_2$$
# 
# And then:
# $$\ddot{x}_{1} = -\left(\dfrac{k}{m}+\dfrac{k'}{m}\right) x_1 + \dfrac{k'}{m}x_2$$
# $$\ddot{x}_{2} = \dfrac{k'}{m}x_1 - \left(\dfrac{k}{m}+\dfrac{k'}{m}\right)x_2$$
# 
# This is a linear differential equation. That means we can represent it as a vector equation:
# 
# $$\ddot{\mathbf{x}} = \pmb{A} \mathbf{x}$$
# 
# where $\pmb{A}$ will represent the different coefficients in our differential equation. Below we write the matrix representation of the same equation above:
# 
# $$\begin{bmatrix}
# \ddot{x}_1\\
# \ddot{x}_2
# \end{bmatrix} = \begin{bmatrix}
# -\left(\dfrac{k}{m}+\dfrac{k'}{m}\right) & +\dfrac{k'}{m}\\
# +\dfrac{k'}{m} & -\left(\dfrac{k}{m}+\dfrac{k'}{m}\right)
# \end{bmatrix}
# \begin{bmatrix}
# {x}_1\\
# {x}_2
# \end{bmatrix}
# $$
# 
# When all the springs are the same $k$, you will show in class this leads to two normal modes with frequencies:
# 
# $$\omega_1^2 = \dfrac{k}{m}$$
# $$\omega_2^2 = \dfrac{3k}{m}$$
# 
# 

# ## Book Readings
# 
# This reading is useful preparation for our normal modes discussion.
# 
# ### Crawford's Waves book - Secs. 1.1-1.5
# 
# This book is a great resource for learning about oscillations and waves. Unfortunately, it is out of print. The first section of this book was assigned on the first week ([Secs. 1.1-1.3](https://github.com/dannycab/phy415msu/blob/main/MMIPbook/assets/pdfs/scans/Crawford-Waves-Secs_1.4-1.5.pdf); **Click Download**). If you want a reminder about oscillations from Crawford's perspective, please review that. But read [Sections 1.4-1.5](https://github.com/dannycab/phy415msu/blob/main/MMIPbook/assets/pdfs/scans/Crawford-Waves-Secs_1.4-1.5.pdf); **Click Download**) for class. It will introduce the concept of normal modes, which we will discuss with a short lecture and example that you work on Tuesday. And it will show a phenomenon that we will explore Thursday: [Beats](https://en.wikipedia.org/wiki/Beat_(acoustics))
# 
# ## Video Resources
# 
# If you are a feeling that you would like a little more on oscillations, beats, and matrices before we have class. Check out this video.

# In[3]:


from IPython.display import YouTubeVideo
YouTubeVideo("I0YACDaY-ww", 800, 600)

