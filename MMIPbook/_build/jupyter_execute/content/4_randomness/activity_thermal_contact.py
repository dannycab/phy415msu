#!/usr/bin/env python
# coding: utf-8

# # 1 Dec 2022 - Model of Two Bodies in Thermal Contact
# 
# We've developed an equation for the number of ways we can arrange a small amount of quanta on a small number of oscillators. The formula we developed for arranging $q$ on $N$ oscillators is given below:
# 
# $$\Omega = \dfrac{(q+N-1)!}{q!(N-1)!}$$
# 
# These calculations are only tractable with pencil and paper when the number of quanta and oscillators is low. For even a few hundred oscillators and quanta the calculations can only be done on a computer. In fact, we will see with this model how we can easily blow out our computational tools as well.
# 
# ## Microstates and Macrostates
# 
# Remember that a particular arrangement of quanta on oscillators is a microstate. That is, atom 1 has 3 oscillators with 1 quanta each on oscillator 1 and oscillator 2. But another microstate with quanta each on oscillator 2 and 3 would be the same energy macrostate for atom 1. We typically use energy for our marker for macrostates, but this doesn't have to be the case because micro and macrostate ideas apply well beyond thermal physics to information theory, data science, networks, and general probability theory.
# 
# ## The setup
# 
# Consider two blocks of material made of simple atomic oscillators that can take on quanta of energy. One block has 200 such atoms, and the other block has 300 such atoms. There are 400 quanta of energy that can be distributed between the two. 
# 
# Before we computed the number of ways for a pair of systems, showing that multiplying the ways was how to find the total number. Here we consider the number of total atoms as given, so the number of ways is a function of the number of energy quanta distributed on atom 1 ($q_1$) and the total available ($q_{tot}$).
# 
# $$\Omega_T(q_{tot},q_1) = \Omega_1(q_1)*\Omega_2(q_{tot}-q_1)$$
# 
# Your goal is to compute the number of total ways to distribute $q_1$ quanta given $q_{tot}$ available and plotting the distribution $\Omega_T$ as a function of $q_1$.

# Some steps:
# 
# * Write a function that computes the number of ways given a $q$ and $N$
# * Test that function on small $q$ and $N$ that we've used
# * Write a function that calls the above one but sweeps through the number of quanta $q$
# * Show you can reproduce the small distribution that we did by hand
# * Plot the distribution of number of ways for the 200/300 oscillator setup with 400 quanta
# * Try to break your code by increasing these numbers.

# In[1]:


## your code here


# 
