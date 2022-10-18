#!/usr/bin/env python
# coding: utf-8

# # 3 - Oscillations with Many Degrees of Freedom
# 
# Coupled oscillations are quite common in nature; collections of objects and larger systems exhibit oscillatory behavior frequently. At times, the number of objects in a system that are oscillating are so many that we begin to zoom out and look at the behavior not of individual elements but of larger collections. This is moving to a continuum view of this oscillatory behavior. Consider going from 1 SHO, to two coupled SHO, to N coupled SHOs where N is very large, and, finally to a rope. It seems like there is a connection between a rope and a set of SHOs. Indeed, we can develop the wave equation for a rope using this kind of modeling. That is a well-known result, so we will instead use it. We start with motivating ourselves with how important waves are to our understanding of nature.

# In[1]:


from IPython.display import YouTubeVideo
YouTubeVideo("hebGhsNsjG0", 800, 600)


# ## Gravitational Waves
# 
# Predicted by the [General Theory of Relativity](https://en.wikipedia.org/wiki/General_relativity) but only [observed 7 years ago](https://news.mit.edu/2016/ligo-first-detection-gravitational-waves-0211), [gravitational waves](https://en.wikipedia.org/wiki/First_observation_of_gravitational_waves) are not only a critical finding in our search to understand the universe, but also a new [way to observe] the universe! These waves ripple through space time, disrupting matter on the smallest of scales. The LIGO detector's strain sensitivity (how small a deformation it can detect) is incredible. At scale, LIGO can detect a change in length about the width of your thumb over a distance that would be between us and the next closest galaxy. That is incredibly sensitive.
# 
# ```{admonition} Discovery of Gravitation Waves
# The work to find measure gravitational waves has been a long effort. Since the prediction of these waves by Einstein in 1916, folks have tried to push experimentalists to construct a detector. Enter LIGO, the massive gravitational wave observatories in Louisiana and Washington State. These detectors were discussed since the 1960s! But only started to be developed in the late 1990s. These detectors consist of two 3km long interferometers that measure the time of flight between ends of the detectors. The length is needed because the changes are so small! They came online in 2002, observing the first gravitational wave on 14 Sept 2015 at 5:51AM ET. 
# 
# One scientist who lead the LIGO team and has been instrumental in the work of LIGO since then is [Nergis Mavalvala](https://physics.mit.edu/faculty/nergis-mavalvala/). She is a MacArthur award winning scientist who directed the first successful LIGO mission. While the [2017 Nobel prize](https://www.nobelprize.org/prizes/physics/2017/press-release/) went to the Rainer Weiss, Barry Barish and Kip Throne for their pioneering work on gravitational waves including immense contributions to the design and development of LIGO, it was Mavalvala who directed the mission.
# ```

# ## The Wave Equation
# 
# There are _many_ wave equations. They simply describe the relationship between how something changes in space and time. It is a specific relationship that relates the influences (e.g., forces, electric interactions, viscosity, etc.) to what we can observe (e.g., changes in height, frequency, color, or number). But the one to being with is the the most basic one. By basic, we do not mean that it is simple but rather that it is the basis for many other wave equations. This is the 1D wave equation for a rope:
# 
# $$\dfrac{\partial^2 h(x,t)}{\partial t^2} = \dfrac{T_0}{\rho_0}\dfrac{\partial^2 h(x,t)}{dx^2}$$
# 
# The function $h(x,t)$ represent the height of the string relative to some zero line both along the strong (in the $x$ direction) and over time (as $t$ marches forward).
# 
# Solving this equation in general can be done using a standing wave solution - the continuous analog to our normal modes approach for coupled oscillators. We can guess the mode will be oscillatory and derive the resulting general solution. This is done in the principal reading below, which comes from Crawford's Waves book.

# ## Reading
# 
# Crawford's book is excellent here, but derives the equation from first pricniples. This is important physics, but I do not expect you to develop such a model from scratch. It is an important derivation that shows how we start many PDE problems. More important to our work those is what appears from pages 54 forward. The solutions and their meaning. We will get to using Fast Fourier Transforms starting from this, but you don't need to read about the Fourier Analysis yet. Just focus on Secs. 2.1-2.2 and the first parts of 2.3.
# 
# * [Crawford Sec 2.1-2.3](https://github.com/dannycab/phy415msu/blob/main/MMIPbook/assets/pdfs/scans/Crawford-Waves-Sec_2.1-2.3.pdf); **Click Download**
# 
# 
# ## More Resources
# 
# The video below covers the Crawford's book in the first 30 minutes. The instructor speaks quickly, but the content is solid and follows what you'll read fairly well. If you want more of the mathematical background, watch this video for sure. We will cover some of it in class, but you are not expected you to derive it.

# In[2]:


from IPython.display import YouTubeVideo
YouTubeVideo("1JeBWHzrRD4", 800, 600)


# In[ ]:




