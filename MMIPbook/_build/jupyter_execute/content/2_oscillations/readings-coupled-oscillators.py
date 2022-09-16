#!/usr/bin/env python
# coding: utf-8

# # Coupled Oscillators
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
YouTubeVideo("7fgKBJDMO54", 800, 600)


# ## Neutrino Oscillations
# 
# These [neutrino oscillations](https://en.wikipedia.org/wiki/Neutrino_oscillation) are incredibly important to the future of high energy and particle physics. Because of their observed oscillation, it is clear the neutrino is not a massless particle, but how much mass is an open question. The work that lead to this discovery was lead by Takaaki Kajita and Arthur McDonald who jointly were awarded the [2015 Nobel Prize in physics](https://www.nobelprize.org/prizes/physics/2015/press-release/).
# 
# ```{admonition} Current Research at Michigan State
# The Physics and Astronomy Department at MSU has a research effort devoted to neutrinos and neutrino oscillations. Some of this work is lead by [Prof. Kendall Mahn](https://www.dunescience.org/facesofdune/kendall-mahn/) who works on the [Deep Underground Neutrino Experiment (DUNE)](https://www.dunescience.org/). The work of her and her team have the potential to [break standard model physics](https://www.scientificamerican.com/article/is-the-standard-model-of-physics-now-broken/) and move us into the realm of new particle physics.
# ```
