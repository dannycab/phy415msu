#!/usr/bin/env python
# coding: utf-8

# # 29 Nov 2022 - Markov Chain Monte Carlo Modeling
# 
# One of the principal tools we have at our disposal when it comes to systems with randomness is the Monte Carlo simulation. Monte Carlo is a large class of approaches that all rely on probabilistic outcomes to determine results. In physics, we often use Monte Carlo to find integrals or sums that we are unable to compute by hand. 
# 
# ## Markov Chain Monte Carlo
# 
# We often find ourselves using a type of Monte Carlo simulation that makes use of a Markov Chain. This is called the MCMC model. The mathematical foundations of Markov Chains are well beyond the scope of this course, but the principal issue is that we want to describe is how this simulation works. The video below describes the conceptual backing of MCMC and how it was first used in physics in 1953 to develop a model of an ideal gas. We will make a similar model!

# In[1]:


from IPython.display import YouTubeVideo
YouTubeVideo("12eZWG0Z5gY", 800, 600)
## If embed doesn't work just click to go to YouTube


# ## Statistical Mechanics
# 
# MCMC is used in lots of statistical mechanics problems because they are fundamentally probabilistic by nature. Starting with the "chance" of finding our system in a given state (with known energy, $E_i$) at a known temperature (T) given by the Boltzmann factor:
# 
# $$e^{-E_i/{k_b T}}$$
# 
# where $k_b$ is the Boltzmann constant. Through this, we developed a statistical model where we found that the normalized probability of finding your system in a state $s$ with energy $E_s$ (just using the $s$ to indicate a state) is given by:
# 
# $$P(s) = \dfrac{1}{Z} e^{-E_s/{k_b T}}$$
# 
# where $Z$ is the partition function, a constant for a given temperature that normalizes our calculation. It is a sum over all states:
# 
# $$Z = \sum_s e^{-E_s/{k_b T}}$$
# 
# Our analysis relied on the development of a statistical theory of mechanics, and we illustrated it with an ideal gas. Notes appear below:
# 
# * [Introduction to Stat. Mech.](https://github.com/dannycab/phy415msu/blob/main/MMIPbook/assets/pdfs/notes/Notes_4_Intro_to_Stat_Mech.pdf)
# * [The Ideal Gas](https://github.com/dannycab/phy415msu/blob/main/MMIPbook/assets/pdfs/notes/Notes_4_Ideal_Gas_Model.pdf)
# 
# Because $P(S)$ is a probability we can use it find average values (expectation values) of a thermodynamic system. We did this for energy using the thermodynamic relations in the notes. But we can also use statistical properties to find the same. For example, finding the expected internal energy of a system, $\langle U \rangle$, just involves adding up all the possible energy states multiplied by their probabilities!
# 
# $$\langle U \rangle = \sum_s E_s P(s)$$
# 
# When these sums are really hard to compute because there's lots of states or only a few that contribute substantially (as in the case for large systems), we can use selective sampling, which is the basis for MCMC. We will discuss that conceptually in class before using MCMC.

# 
