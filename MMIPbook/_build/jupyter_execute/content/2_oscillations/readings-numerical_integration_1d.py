#!/usr/bin/env python
# coding: utf-8

# # 2 - Numerical Integration in 1D
# 
# Principal Ideas come from [Newman Chapter 8, Section 1]
# 
# 
# We have seen how we can quickly exhaust our analytical tools when we investigate systems with interesting and complex behavior. We can see much from the perspective of phase space in terms of the qualitatively different behaviors (e.g., oscillations vs rotations, both clockwise and counter-clockwise, in the large angle pendulum). But what if we can to find the trajectory of a given system.
# 
# That is how can we take a general differential equation:
# 
# $$\ddot{x} = f(x,\dot{x},t)$$
# 
# to $x(t)$? in (most) cases...because sometimes integrals don't converge.
# 
# We can use **numerical integration** to do so. Below is a video describing 3 coupled ODEs, the Lorenz equations, that are quite famous. You will be able to model systems like this, but for now think of it as motivation for why we want to learn numerical integration.

# In[1]:


from IPython.display import YouTubeVideo
YouTubeVideo("aAJkLh76QnM", 800, 600)


# ## Nonlinear Dynamics and Chaos
# 
# Some of the most interesting problems to work on are 
# 

# ## Book Readings
# 
# These two readings are useful preparation for what we are going to do with numerical integration. 
# 
# ### Newman's Computational Physics - Chapter 8
# 
# The first one is from [Chapter 8 of Mark Newman's book, Computational Physics](https://github.com/dannycab/phy415msu/blob/main/MMIPbook/assets/pdfs/scans/Newman_Ch8_ODEs.pdf), which is an excellent introduction to most of the computational physics approaches we use in physics. It uses Python and modern libraries, which is rare for a computational physics textbook for undergraduate students.
# 
# **Read This** Sections 8.1 and 8.1.1. We will discuss and work with ideas from 8.1.2 and 8.1.3, but I don't expect you to read those in detail. We will discuss how these work and then make use of the [built-in integrators from scipy](https://docs.scipy.org/doc/scipy/tutorial/integrate.html). The core one will be ```odeint``` [(Documentation)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html?highlight=odeint).
# 
# ### Strogatz's Nonlinear Dynamics and Chaos - Chapters 4 and 5
# 
# The second one in from [Chapters 4 and 5 of Steven Strogatz's book, Nonlinear Dynamics and Chaos](https://github.com/dannycab/phy415msu/blob/main/MMIPbook/assets/pdfs/scans/Strogatz_Integrating_Ch4-5.pdf), which is an excellent and broad book covering many science and engineering problems. It is a book that I think every student of physics should read at some point.
# 
# **Read This** Section 5.1. We have worked already with these ideas, but we will continue to do so. This is another way to look at what we've done, so it's worth reading another perspective. We will continue to discuss and work with these ideas. You are free to read other parts of this book, but please read 5.1 for class.
