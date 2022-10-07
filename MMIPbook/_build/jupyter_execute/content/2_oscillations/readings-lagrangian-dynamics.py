#!/usr/bin/env python
# coding: utf-8

# Book Reading: Any Classical Mechanics Book
# 
# # 4 Oct 22 - Notes: Lagrangian Dynamics
# 
# [Newtonian Mechanics](https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion) is an incredibly useful model of the natural world. In fact, it wasn't until the mid 1970s that we were able to truly [test Einstein's gravity as a true replacement](https://en.wikipedia.org/wiki/Tests_of_general_relativity) for Newton. That being said, for most terrestrial situations (macroscopic objects moving at low speeds), Newton's mechanics is very good. However, the problem with Newton is that it requires a few things:
# 
# 1. We must be able identify each interaction on the object or model an average behavior from many littler interactions (e.g., models of friction vs. detailed E&M forces)
# 2. We must be able to mathematically describe the size and direction of the interaction at all times we want to model
# 3. We must be able to vectorially add the interactions to produce the net force $\sum_i \vec{F}_i = \vec{F}_{net}$.
# 
# In many cases, we can do this. But consider the picture below of a bead sliding inside a cone. How would you write down the contact force between the cone and the bead for all space and time?
# 
# ![Cone](../../assets/images/cylindrical_cone_mass.jpg)
# 
# 

# Enter the [Lagrangian Mechanics](https://en.wikipedia.org/wiki/Lagrangian_mechanics), an equivalent descirption of Newton's mechanics developed through several adbances in physics and mathematics in the 17th and 18th centuries. Some of the major contributors included Newton, Gottfried Wilhelm Leibniz, Pierre Louis Moreau de Maupertuis, Guillaume de l'Hôpital, Jacques Bernoulli, Jean Bernoulli, and Jean D'Alembert. This period of the development of mechanics was foundational to the development of concepts like the [action](https://en.wikipedia.org/wiki/Action_(physics)) and [phase space](https://en.wikipedia.org/wiki/Phase_space) as well as approaches like [variational analysis](https://en.wikipedia.org/wiki/Calculus_of_variations), which formed the basis for [dynamical systems](https://en.wikipedia.org/wiki/Dynamical_system) (phase space describes real motion), [quantum mechanics](https://en.wikipedia.org/wiki/Quantum_mechanics) (quantize the action), and [perturbation theory](https://en.wikipedia.org/wiki/Perturbation_theory) (approximate answers can be iteratively sought).

# This analysis is grounded in optimization or rather extremization. The idea is as follows:
# 
# 1. Consider all potential paths a system can take through phase space
# 2. Time each of them between the same two points in phase space
# 3. The one that minimizes the action integral over that time/space is the one the system takes
# 
# This might seem magical! But it's truly a deep connection to the energetics of the system, which limit the the relevant equations of motion by both the number of degrees of freedom (ways the system can move) and the constraints equation (things that influence the motion).
# 
# Parth G. has a lovely video below in his dulcet tone about the basics of this as we talked in class.

# In[1]:


from IPython.display import YouTubeVideo
YouTubeVideo("KpLno70oYHE", 800, 600)


# 
# 
# My notes go into detail on the development of the Lagrangian problem. But practice is the best approach.
# 
# 
# 
# 
# ## Book Readings
# 
# This reading is useful preparation for reminding yourself of Lagrangian Dynamics.
# 
# * Any classical mechanics book you like! Taylor is a good one.
# * [A Google Book you can review](https://www.google.com/books/edition/A_Student_s_Guide_to_Lagrangians_and_Ham/ebTCAQAAQBAJ?hl=en&gbpv=1&dq=lagrangian+dynamics+book&printsec=frontcover)
# 
# ## Handwritten Notes
# 
# Here are my handwritten notes on coupled oscillations and normal modes.
# 
# * [Lagrangian Dynamics](https://github.com/dannycab/phy415msu/blob/main/MMIPbook/assets/pdfs/notes/Notes_2_Lagrangian_Dynamics.pdf)
# * [Lagrangian Example](https://github.com/dannycab/phy415msu/blob/main/MMIPbook/assets/pdfs/notes/Notes_2_Lagrangian_Example.pdf)
# * [Lagrangian Example with Generalized Forces](https://github.com/dannycab/phy415msu/blob/main/MMIPbook/assets/pdfs/notes/Notes_2_Lagrangian_Example_Gen_Force.pdf)
# 
# ## Video Resources
# 
# If you are a feeling that you would like a little direct instruction on this, this lecture is great. Lots of examples!

# In[2]:


from IPython.display import YouTubeVideo
YouTubeVideo("zhk9xLjrmi4", 800, 600)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




