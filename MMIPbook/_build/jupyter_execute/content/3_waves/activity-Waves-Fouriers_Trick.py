#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# # 27 Oct 2022 - Activity - Deconstructing Waves
# 
# While we observe waves in many places, it's the case that we don't often have the luxury of constructing them as we want. In fact, much of the science we do relies on measurements of voltage or current to represent the dynamics of the system. 
# 
# * Want to measure distance? Interferometry gives you a voltage to calibrate.
# * Want to measure material surface properties? Voltage jumps across probes give you proxies
# * Viscosity? Stick the stuff in a rheometer, squeeze it, and measure voltage changes.
# * AYO exoplanets? Light curves are really just measures of voltage across a CCD.
# 
# The point is that you will almost always be dealing with signals that are proxies for the actual thing you care about. So let's construct some and deconstruct them.
# 
# Below is the code that we developed last class to investigate the signals we produced.

# In[2]:


t = np.linspace(0,2,1000)
omega1 = 100
omega2 = 105
omega3 = 1000

A1 = 1
A2 = 0.9
A3 = 0.1

y1 = A1*np.cos(omega1*t)

y2 = A2*np.cos(omega2*t)
y3 = A2*np.cos(omega3*t)
y4 = A3*np.cos(omega2*t)
y5 = A3*np.cos(omega3*t)

CloseAmpCloseFreq = y1+y2
CloseAmpFarFreq = y1+y3
FarAmpCloseFreq = y1+y4
FarAmpFarFreq = y1+y5


# In[3]:


fig = plt.figure(figsize=(16,8))


plt.plot(t,CloseAmpCloseFreq+6, label='Close Amp; Close Freq')
plt.plot(t,CloseAmpFarFreq+2, label='Close Amp; Far Freq')
plt.plot(t,FarAmpCloseFreq-2, label='Far Amp; Close Freq')
plt.plot(t,FarAmpFarFreq-6, label='Far Amp; Far Freq')

plt.legend()


# ## Questions:
# 
# 1. Adjust the signals to show qualitatively how the different signals behave as you change frequencies and amplitudes.
# 2. Build a table that discusses qualitatively what happens as each change is made. We will compile this table together.

# ## Dealing with "Real" Signals
# 
# Ok, but can we find these frequencies given a signal? Or rather, how might we find the signal we need? We can use a little mathematics from Fourier.
# 
# Any periodic function in 1 dimension can be expanded as a general sum of sines and cosines:
# 
# $$f(t) = \dfrac{a_0}{2} + \sum_{n=1}^{\infty} \left(a_n sin(\omega_n t) + b_n cos(\omega_n t) \right)$$
# 
# We can show this can be written like:
# 
# $$f(t) = \sum_{-\infty}^{+\infty} c_n e^{i\omega_n t}$$
# 
# But how does this get us what we need? Our goal is to find the expansion coefficients ($a_n$'s & $b_n$'s or just the $c_n$'s), which tells us the right mix of signals to add together to get the observed one. Why is that important? Consider the signals below? How might we analyze them?

# In[4]:


from scipy.signal import sawtooth, square, chirp

t = np.linspace(0,10,1000)

saw = sawtooth(t)
sq = square(t)
ch = chirp(t,6,10,1)

fig = plt.figure(figsize=(12,8))
plt.plot(t, saw, label="Sawtooth Wave")
plt.plot(t, sq+3, label='Square Wave')
plt.plot(t, ch-3, label='Chirp')
plt.legend()


# ## Integration Activity
# 
# Consider the Fourier Expansion of your choosing:
# 
# $$f(t) = \dfrac{a_0}{2} + \sum_{n=1}^{\infty} \left(a_n \sin(\omega_n t) + b_n \cos(\omega_n t) \right) \qquad f(t) = \sum_{-\infty}^{+\infty} c_n e^{i\omega_n t}$$
# 
# In terms of the longest period, $T_0$,
# 
# $$f(t) = \dfrac{a_0}{2} + \sum_{n=1}^{\infty} \left(a_n \sin(\dfrac{2n\pi t}{T_0}) + b_n \cos(\dfrac{2n\pi t}{T_0}) \right) \qquad f(t) = \sum_{-\infty}^{+\infty} c_n e^{i\dfrac{2n\pi t}{T_0}}$$
# 
# Find the expansion coefficients for the following signals (think before you integrate):
# 
# 1. $f(t) = \cos(\omega_0 t)$ here $\omega_0$ corresponds to the longest known period $T_0$.
# 2. $f(t) = 2\sin(\omega_0 t) + 3\cos(2*\omega_0t)$
# 3. $f(t) = 2\sin(\omega_0 t+\pi/2) + 3\cos(2*\omega_0t)$
# 4. $f(t) = 1$ from 0 to $T_0/2$ and 0 from $T_0/2$ to $T_0$ repeating.... 
# 
# 

# ## 1D Integration
# 
# It's not great doing this by hand. Certainly, we can pick off the first two easily because they match our model easily. What about the 3rd one?
# 
# $$f(t) = 2\sin(\omega_0 t+\pi/2) + 3\cos(2*\omega_0t)$$
# 
# It's clever to change this to a cosine and read off the values:
# 
# $$f(t) = 2\sin(\omega_0 t+\pi/2) + 3\cos(2*\omega_0t) = 2\cos(\omega_0 t) + 3\cos(2*\omega_0t)$$
# 
# And thus: $b_1 = 2$ and $b_2=3$ and everything else vanishes.
# 
# Can we do the integrals and get the same results? Let's form the integrals we need to do this. The left hand side uses the real function $f(t)$, the right hand side replaces it with the model of $f(t)$ expanded over sine and cosine harmonics.

# ### Integrals that solve this problem
# 
# **We start with the sine function first:**
# 
# $$\int_0^{T_0}f(t)\sin\left(\dfrac{2m\pi}{T_0}{t}\right)\;dt = \int_0^{T_0} \left(\dfrac{a_0}{2} + \sum_{n=1}^{\infty} \left(a_n \sin(\dfrac{2n\pi t}{T_0}) + b_n \cos(\dfrac{2n\pi t}{T_0}) \right)\right) \sin\left(\dfrac{2m\pi}{T_0}{t}\right)\;dt$$
# 
# $$\int_0^{T_0}f(t)\sin\left(\dfrac{2m\pi}{T_0}{t}\right)\;dt = \int_0^{T_0} \left(\dfrac{a_0}{2}\right) \sin\left(\dfrac{2m\pi}{T_0}{t}\right) dt + \int_0^{T_0} \sum_{n=1}^{\infty} a_n sin\left(\dfrac{2n\pi t}{T_0}\right) \sin\left(\dfrac{2m\pi}{T_0}{t}\right) dt + \int_0^{T_0}  \sum_{n=1}^{\infty} b_n cos\left(\dfrac{2n\pi t}{T_0}\right) \sin\left(\dfrac{2m\pi}{T_0}{t}\right) dt $$
# 
# Notice we get three integrals on the right side (where we moved the integral inside the sum as we can do and focus on the $n$ th term):
# 
# $$\int_0^{T_0} \left(\dfrac{a_0}{2}\right) \sin\left(\dfrac{2m\pi}{T_0}{t}\right) dt = 0\qquad \mathrm{(sinusoidal\;over\;the\;standard\;interval)}$$
# 
# $$a_n \int_0^{T_0} \sin\left(\dfrac{2n\pi}{T_0}t\right) \sin\left(\dfrac{2m\pi}{T_0}{t}\right) dt = a_n\dfrac{T_0}{2}\;\mathrm{(for\;n=m,\;0\;otherwise)}$$
# 
# $$b_n \int_0^{T_0}  \cos\left(\dfrac{2n\pi}{T_0}t\right) \sin\left(\dfrac{2m\pi}{T_0}{t}\right) dt = 0 $$
# 
# The left side uses the real $f(t)$ (note that when $n=m$ provides the only nonzero terms):
# 
# $$\int_0^{T_0}f(t)\sin\left(\dfrac{2n\pi}{T_0}{t}\right)\;dt = \int_0^{T_0} \left(2\sin(\omega_0 t+\pi/2) + 3\cos(2\omega_0t)\right) \sin\left(\dfrac{2n\pi}{T_0}{t}\right)\;dt$$
# 
# $$=\int_0^{T_0} 2\sin(\dfrac{2\pi}{T_0} t+\pi/2) \sin\left(\dfrac{2n\pi}{T_0}{t}\right)\;dt + \int_0^{T_0}  3\cos(2\dfrac{2\pi}{T_0}t) \sin\left(\dfrac{2n\pi}{T_0}{t}\right)\;dt $$
# 
# $$=\dfrac{2nT_0\sin^2(n\pi)}{\pi(n^2-1)} + \dfrac{3nT_0\sin^2(n\pi)}{\pi(n^2-4)} = a_n\dfrac{T_0}{2}$$
# 
# Thus, all the $a_n$'s are zero as when we combine the two sides we get:
# 
# $$a_n\dfrac{T_0}{2} = 0$$

# ### More integrals that solve this problem
# 
# **Now the cosine function:**
# 
# $$\int_0^{T_0}f(t)\sin\left(\dfrac{2m\pi}{T_0}{t}\right)\;dt = \int_0^{T_0} \left(\dfrac{a_0}{2} + \sum_{n=1}^{\infty} \left(a_n \sin(\dfrac{2n\pi t}{T_0}) + b_n \cos(\dfrac{2n\pi t}{T_0}) \right)\right) \cos\left(\dfrac{2m\pi}{T_0}{t}\right)\;dt$$
# 
# $$\int_0^{T_0}f(t)\cos\left(\dfrac{2m\pi}{T_0}{t}\right)\;dt = \int_0^{T_0} \left(\dfrac{a_0}{2}\right) \cos\left(\dfrac{2m\pi}{T_0}{t}\right) dt + \int_0^{T_0} \sum_{n=1}^{\infty} a_n \sin\left(\dfrac{2n\pi t}{T_0}\right) \cos\left(\dfrac{2m\pi}{T_0}{t}\right) dt + \int_0^{T_0}  \sum_{n=1}^{\infty} b_n \cos\left(\dfrac{2n\pi t}{T_0}\right) \cos\left(\dfrac{2m\pi}{T_0}{t}\right) dt $$
# 
# Notice we get three integrals on the right side (where we moved the integral inside the sum as we can do and focus on the $n$ th term):
# 
# $$\int_0^{T_0} \left(\dfrac{a_0}{2}\right) \cos\left(\dfrac{2m\pi}{T_0}{t}\right) dt = 0\qquad \mathrm{(sinusoidal\;over\;the\;standard\;interval)}$$
# 
# $$a_n \int_0^{T_0} \sin\left(\dfrac{2n\pi}{T_0}t\right) \cos\left(\dfrac{2m\pi}{T_0}{t}\right) dt = 0$$
# 
# $$b_n \int_0^{T_0}  \cos\left(\dfrac{2n\pi}{T_0}t\right) \cos\left(\dfrac{2m\pi}{T_0}{t}\right) dt = b_n\dfrac{T_0}{2} \;\mathrm{(for\;n=m,\;0\;otherwise)}$$
# 
# The left side uses the real $f(t)$ (note that when $n=m$ provides the only nonzero terms):
# 
# $$\int_0^{T_0}f(t)\cos\left(\dfrac{2n\pi}{T_0}{t}\right)\;dt = \int_0^{T_0} \left(2\sin(\omega_0 t+\pi/2) + 3\cos(2\omega_0t)\right) \cos\left(\dfrac{2n\pi}{T_0}{t}\right)\;dt$$
# 
# $$=\int_0^{T_0} 2\sin(\dfrac{2\pi}{T_0} t+\pi/2) \cos\left(\dfrac{2n\pi}{T_0}{t}\right)\;dt + \int_0^{T_0}  3\cos(2\dfrac{2\pi}{T_0}t) \cos\left(\dfrac{2n\pi}{T_0}{t}\right)\;dt $$
# 
# $$=\dfrac{nT_0\sin(2n\pi)}{\pi(n^2-1)} + \dfrac{3nT_0\sin(2n\pi)}{2\pi(n^2-4)} = b_n\dfrac{T_0}{2}$$

# 
