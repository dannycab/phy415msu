#!/usr/bin/env python
# coding: utf-8

# ```{bibliography}
# :style: unsrt
# ```
# 
# # The Simple Harmonic Oscillator
# 

# ## The SHO model
# 
# From these observations we find that a reasonable force model for a 1D spring system is given by:
# 
# $$F_{spring} = -k |x-x_0|$$
# 
# where $k$ is the spring constant for the spring and $x_0$ is the equilibrium location. As we know from Newton's second law, if we can argue that this force is the only force or the dominant behavior we are trying to model in a mechanical situation, we have the following ordinary differential equation:
# 
# $$F_{net} = F_{spring}$$
# $$m\ddot{x} = -k|x-x_0|$$
# 
# Without much loss, we can recast the problem in terms of the distance from equilbirium ($s=|x-x_0|$). *As you will learn this is not a problem from vertically hanging springs near the surface of the Earth because the graviational force is constant and depends on the mass of the hanging weight.*
# 
# ```{admonition} The SHO mathematical model
# $$m\ddot{s} = -ks$$
# ```
# 
# ### Finding the general solution
# 
# We can solve this using our typical approach to 2D linear ODEs; guess the form of the solution and check it.
# 
# $$\ddot{s} = -\frac{k}{m}s$$
# 
# Assume: $s(t) = A\exp(i\omega t)$ As we will learn this form is a good guess for linear ODEs. This gives:
# 
# $$\ddot{s} = -\omega^2\;A\exp(i\omega t)$$
# 
# So that,
# 
# $$-\omega^2\;A\exp(i\omega t) = -\frac{k}{m}A\exp(i\omega t)$$
# 
# This solution is consistent with the model (i.e., solves the differential equation) if we set $\omega$ and notice it is exclusively positive:
# 
# $$\omega^2 = \frac{k}{m} > 0$$
# 
# Thus, $s(t) = A\exp(i\sqrt{\frac{k}{m}} t)$ is **a solution** to this problem. Notice we have to set $A$ using initial conditions for the problem. This is called a **initial value problem** in mathematics. You likely have heard about the Euler formulation; it is one of the most important relationships in mathematics {cite}`nahin2011dr, stipp2017most`. We will get into it more later. It appears below:
# 
# ```{admonition} Leonhard Euler's famous formula
# $$\exp{i\theta} = \cos{\theta} + i \sin{\theta}$$
# ```
# 
# 
# Thus, we know that our solution gives rise to real sinusoidal solutions of the form:
# 
# $$s(t) = A\left(cos{\sqrt{\frac{k}{m}} t} + i\sin{\sqrt{\frac{k}{m}} t}\right)$$
# 
# This probably doesn't look quite right...there's an $i$ in the solution for real physical motion! We will get to that, but we need the initial conditions to do so. More importantly, there's only one free parameter in our current solution, $A$. Given that this equation is **a solution, is it the only solution?**
# 
# ### The order of your differential equation matters
# 
# You probably already know that our general solution for the SHO is:
# 
# $$s(t) = A\exp(i\sqrt{\frac{k}{m}} t) + B\exp(-i\sqrt{\frac{k}{m}} t)$$
# 
# Or written in a way that is more often presented:
# 
# $$s(t) = A'\cos(\sqrt{\frac{k}{m}} t) + B'\sin(\sqrt{\frac{k}{m}} t)$$
# 
# where we have made clear that the free parameters $A$ and $B$ are not equal to $A'$ and $B'$, respectively. Regardless, notice there's two free parameters in these formula. That is because we are solving a **two dimensional** linear ODE. Because there's two derivatives on $s$ (i.e., $\ddot{s}$), we expect to have two free parameters that are set by the intial conditions. This is characteristic of an **initial value problem**.
# 
# ```{admonition} Important Tip
# :class: tip
# The number of free parameters that are set by problem conditions in an initial value problem is determined by the order of the differential equation. 
# 
# Second order? Two conditions needed. Two free parameters to determine. Fourth order? Four conditions needed. Four free parameters to determine.
# ```

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




