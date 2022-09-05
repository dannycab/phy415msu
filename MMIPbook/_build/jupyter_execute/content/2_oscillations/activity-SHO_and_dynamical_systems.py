#!/usr/bin/env python
# coding: utf-8

# # Activity: Investigating the Simple Harmonic Oscillator
# ## Reminders of the SHO and Introduction to Dynamical Systems
# 
# 
# Look for **&#9989; Do this** 

# ### The SHO mathematical model
# 
# We have seen for the canonical one-dimensional harmonic oscillator is described by the following **2nd order linear** differential equation:
# 
# $$m\ddot{s} = -k{s}$$
# 
# where $s$ represents the distance from the oscillators equilibrium position. It's important to note that this model for a linear restoring force gives rise to at **econd order** differential equation. As you will see, there would be no ability for cycles or recurrent behavior without two dimensions (the two dimensions here are the position, $s$, and velocity of the oscillator, $\dot{s}$). It is also important that the differential equation is **linear**.

# ### Linearity of differential equations
# 
# This is something that is easy to confuse because we use the term **linear** in different ways at different times. In many cases this prompts us to think of a line, so that we might think the only linear differential equations are ones where the variable of interest (in this case the position of the oscillator) appears only *linearly* in the equation. 
# 
# :::{warning}
# So you might think that Nth order differential equations of the form:
# 
# $$\dfrac{d^n x}{dt^n} = c\;x$$
# 
# are the only ones that are linear. *Note for the harmonic oscillator $n=2$.*
# :::
# 
# **That is not the case and this is key.**
# 
# The linearity refers to the fact that we can write the differential equation as a **linear combination of the derivatives**. 
# 
# :::{tip}
# 
# So an $N$th linear differential equation (e.g., for position and time) can have the general form:
# 
# $$\sum_{i=0}^N a_i(t)\dfrac{d^ix}{dt} = f(t)$$
# 
# where $\dfrac{d^ix}{dt}$ is the $i$th derivative of $x$ (e.g., $i=0$, $\dfrac{d^0x}{dt}=x$; $i=1$, $\dfrac{d^0x}{dt}=\dfrac{dx}{dt}$) The coefficients are allowed to depend explicitly on time (i.e., $a_i(t)$; you have probably seen *constant coefficients* in the past (where $\dfrac{da_i(t)}{dt}=0$, i.e., $a_i(t) =$ constant). In addition, as you can explore later, the system can be driven by a function that depends only on time (e.g., some forcing function, $f(t)$).
# :::

# ### Why does linearity matter?
# 
# Because much of nature can be modeled with linear differential equations (or approximately so) and linear differential equations have really nice solution properties. *The solutions to linear differential equations are **holonomic functions**. This is just a fancy word for functions you know like polynomials, sine, cosine, exponentiale, and some special functions (e.g., Airy, Bessel, hypergeometric). But these solutions are really important because they are smooth as are their derivatives, so they have really nice properties. 
# 
# In many cases, we can lean on strong properties dervied from linearity:
# 
# - [Uniqueness](https://en.wikipedia.org/wiki/Cauchy%E2%80%93Kowalevski_theorem): If we find a solution to the differential equation and it satisfies the boundary/initial conditions, we are guaranteed that this is the only solution.
# - Linear combinations: The linear nature of the differential equation means linear combinations of general solutions are unchanged. We can build solutions from known general solutions.
# 
# ```{admonition} The Cauchy-Kowaleski theorem 
# This theorem is typically called the Cauchy theorem (or the uniqueness theorem) for [Augustin Louis-Cachy](https://en.wikipedia.org/wiki/Augustin-Louis_Cauchy), a French mathematician who contributed much to the field of complex analysis. However, Cauchy only proved this theorem in a special case.  A Russian Mathematician, [Sofya Kovalevskaya](https://en.wikipedia.org/wiki/Sofya_Kovalevskaya), who was the first woman to earn a PhD in Mathematics (earned 1874, University of G&ouml;ttingen), proved the theorem, in general, in her dissertation. 
# 
# **So, it is really the "Kovalevskaya-Cauchy" theorem.**
# ```

# ### General Solution to the SHO
# 
# We can start with the differential equation:
# 
# $$\ddot{x} = -\omega$$
# 
# where $x$ is the position relative to equilibrium and $\omega^2 = k/m$. We know this is a linear, second-order ODE, so we expect the solutions to be [holonomic functions](https://en.wikipedia.org/wiki/Holonomic_function) - that is, many of the functions we have seen before. Moreover, we need something that when we take two derivatives, we get the same functions back.
# 
# *This is a key to suggest $\sin$ and $\cos$ as our proposed linear combination.*
# 
# Now, we have to decide how to do that. Because **ANY** linear combination is a good starting guess, but not all of them a reasonable guesses. How do we decide? 

# #### Discussion Question
# 
# **&#9989; Do this** 
# 
# Below are several choices of potential general solution guesses, called "ansatz" in many books and classes. Which of them will work for us? How do you know? *Discuss with your neighbors* Demonstrate that one solution you chose works.
# 
# $$x(t) = A\cos(\omega t)$$
# $$x(t) = B\sin(\omega t)$$
# $$x(t) = A\cos(\omega t)+B\sin(\omega t)$$
# $$x(t) = B\sin(\omega t+ \phi_B)$$
# $$x(t) = \sum_i^N A_i\cos(\omega_i t) + B_i\sin(\omega_i t)$$
# 
# **What other general solution forms will work?**

# ### Particular Solutions
# 
# Let's pick two general solutions:
# 
# $$x(t) = A\cos(\omega t) + B\sin(\omega t)$$
# 
# $$x(t) = C\sin(\omega_t + \phi_C)$$
# 
# **&#9989; Do this** 
# 
# - For an SHO that is pulled to a point $x_0$ and let go at $t=0$, find the particular solutions using both general forms. **Compare and contrast these solutions with your neighbor.** What do you notice about them? How can they be made compatible with each other?
# - Make a plot (in this notebook) of both solutions for an SHO with frequency of 100Hz that starts at $x_0 =$ 0.1m
# - Adjust the starting location and frequency, what do you notice?
# - **If you have time**, create a solution for an SHO that is put into motion with a velocity of +0.1m/s at $x_0=0$ at $t=0$.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

#################################
# Adjust code to fit your needs #
#################################

t = np.arange(0,10,0.1)
x = t**2

plt.plot(t,x)


# 
