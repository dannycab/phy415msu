#!/usr/bin/env python
# coding: utf-8

# # 29 Nov 22 Monte Carlo Integration
# 
# A useful approach to making models of systems is using randomness to find solutions to problems that are stable or static. One such approach is called [Monte Carlo integration](https://en.wikipedia.org/wiki/Monte_Carlo_integration) that can be used to find particularly problematic integrals. It's a useful pedagogical introduction to what we are attempting to do, use [Monte Carlo approaches](https://en.wikipedia.org/wiki/Monte_Carlo_method) to model thermodynamical systems using the [Metropolis-Hastings algorithm](https://en.wikipedia.org/wiki/Metropolis%E2%80%93Hastings_algorithm).

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import random as random
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Finding Pi
# 
# This is a classic use of Monte Carlo integration that illustrates many of the concepts of the technique. Effectively, we can assume there's a constant (undetermined) that links that the area of a circle and the radius squared. 
# 
# $$A_{circle} = c r^2$$
# 
# We assume it's radius squared as a test because we know that boxes go like length times width and a sqaure with side length $r$ has:
# 
# $$A_{square} = r^2$$
# 
# Thus the ratio of the area of the circle to the area of the sqaure would give the constant!
# $$\dfrac{A_{circle}}{A_{square}} = \dfrac{c r^2}{r^2} = c$$
# 
# This is true for any radius $r$, so we choose $r=1$. We also notice that we can solve this problem in one quadrant and multiple by four.  So let's graph that.

# In[2]:


step = 0.001
x = np.arange(0,1+step,step)
y = np.sqrt(1-x**2)

plt.figure(figsize=(6,6))
plt.plot(x,y)
plt.axis([0, 1, 0, 1])
plt.grid()


# ### The Drop Algorithm
# 
# The concept behind this is watching rain hit the ground and counting the droplets inside and outside a circle. We can simulate this with random drops in the range from 0 to 1 in $x$ and $y$. Let's start with 500 drops. We plot the drops below.

# In[3]:


ndrops = 500
drops = np.zeros([ndrops,2])

for i in range(ndrops):
    
    xrand = random.random()
    yrand = random.random()
    
    drops[i] = xrand,yrand


# In[4]:


plt.figure(figsize=(6,6))
plt.plot(x,y)
plt.scatter(drops[:,0],drops[:,1], c='C1')
plt.axis([0, 1, 0, 1])
plt.grid()


# Notice that some of the drops are outside the curve and some are inside. We can use the formula for a circle of radius 1 to find which are which. 
# 
# $$x^2 + y^2 = 1$$
# 
# If this produce is below 1, the drop is inside the curve; otherwise it's outside. The statement below forms two binary filters. You might have seen something like this before in CMSE 201. We can use those filters on the arrays are replot to confirm.

# In[5]:


outsideCurve = drops[:,0]**2+drops[:,1]**2 > 1
insideCurve = drops[:,0]**2+drops[:,1]**2 < 1


# In[6]:


plt.figure(figsize=(8,8))
plt.plot(x, y, label='circle')
plt.scatter(drops[insideCurve,0],drops[insideCurve,1], c='C1', label='inside')
plt.scatter(drops[outsideCurve,0],drops[outsideCurve,1], c='C2', label='outside')
plt.axis([0, 1, 0, 1])
plt.grid()


# ### Computing Pi
# 
# We assumed our approach would bear out a constant.
# 
# $$c=\dfrac{A_{circle}}{A_{square}}$$
# 
# We can compute an estimate of it using the number of drops, which are proxies for the area of a quarter circle.
# 
# $$c \approx 4\dfrac{N_{inside}}{N}$$
# 
# Our estimate is below.

# In[7]:


pi_estimate = 4*len(drops[insideCurve])/len(drops)
print(pi_estimate)


# ## Seeking Convergence
# 
# So the estimate was probably not great. But we can make it better by choosing more drops. So rewrite this approach a function where you can send the number of drops in and return the estimate of pi. Then use it to plot this estimate over many choices of N. Show what the value converges to.

# In[8]:


def FindPi(ndrops):
    
    drops = np.zeros([ndrops,2])

    for i in range(ndrops):
    
        xrand = random.random()
        yrand = random.random()
    
        drops[i] = xrand,yrand

    outsideCurve = drops[:,0]**2+drops[:,1]**2 > 1
    insideCurve = drops[:,0]**2+drops[:,1]**2 < 1
    
    return 4*len(drops[insideCurve])/len(drops)


# In[9]:


N = 10000
estimates = np.zeros((N,1))

for i in range(1,N):
    
    estimates[i] = FindPi(i)


# In[10]:


plt.figure(figsize=(8,6))
plt.plot(estimates)
plt.axhline(np.pi, 0, N, c='C1')


# ### Let's compute pi
# 
# Ok we can see from the plot that roughly from 2500 to 10000 steps we have something reasonably converged. Let's grab those values and get an estimate of pi.

# In[11]:


start = 2500
pi_avg=np.average(estimates[start:])
pi_stddev=np.std(estimates[start:])

print('Our estimate is:', pi_avg, '+/-', pi_stddev)


# ## Finding the values of integrals
# 
# So that was a cool trick, but the power of this form of Monte Carlo is being able to compute very difficult integrals. It's not efficient as other integrators, but it's sometimes the only choice.
# 
# ### Integrating sine
# 
# Using the same approach as before where we take the proportion of drops 'under the curve' compared to all drops, find the integral of $sin(x)$ over one interval. 
# 
# * Find the number of drops needed to make a reasonable estimate.
# * Use the long term behavior (plot it?) to estimate the value and uncertainty in the integral

# ### Method 1, use symmetry
# 
# Because we know that the integral of sine over one-half interval is the same, we can instead just solve the problem between 0 and $\pi$. The result is then the sum of the two, which we expect to be zero and we force by doing only half. So the estimate we really seek is what is the integral from 0 to $\pi$.
# 
# $$\int_0^{\pi} \sin(x) dx = 2$$

# In[12]:


x=np.arange(0.0001, np.pi, 0.0001)
y = np.sin(x)

ndrops = 500
drops = np.zeros([ndrops,2])

for i in range(ndrops):

    xrand = random.random()*np.pi
    yrand = random.random()

    drops[i] = xrand,yrand
        
ytest = np.sin(drops[:,0])
below_test = drops[:,1] < ytest

plt.plot(x, y)
plt.scatter(drops[~below_test,0],drops[~below_test,1], c='C1')
plt.scatter(drops[below_test,0],drops[below_test,1], color='C2')

L = max(x)
H = max(y)

area = H*L
proportion = len(drops[below_test,:])/len(drops)

print('Our estimate:', proportion*area)


# In[13]:


def FindSine(ndrops):
    
    drops = np.zeros([ndrops,2])

    for i in range(ndrops):
    
        xrand = random.random()*np.pi
        yrand = random.random()
    
        drops[i] = xrand,yrand

    ytest = np.sin(drops[:,0])
    below_test = drops[:,1] < ytest
    
    L = np.pi
    H = 1

    area = H*L
    proportion = len(drops[below_test,:])/len(drops)
    
    return area*proportion


# In[14]:


N = 5000
estimates = np.zeros((N,1))

for i in range(1,N):
    
    estimates[i] = FindSine(i)


# In[15]:


plt.figure(figsize=(8,6))
plt.plot(estimates)
plt.axhline(2, 0, N, c='C1')


# ### Method 2; using windows
# 
# Instead of assuming symmetric, we can use logical binaries to window our data. That is find windows of positive and negative values of the function to compute integrals seperately and then add together. Below we use that technique.

# In[16]:


x=np.arange(0.0001, 2*np.pi, 0.0001)
y = np.sin(x)

ndrops = 5000
drops = np.zeros([ndrops,2])

for i in range(ndrops):

    xrand = random.random()*2*np.pi
    yrand = (random.random()-0.5)*2

    drops[i] = xrand,yrand

less_than_pi = (drops[:,0] < np.pi) ##First half
above_zero = (drops[:,1] > 0) ## Points below zero
less_than_val = (drops[:,1] < np.sin(drops[:,0])) ## below positive curve

first_window = np.logical_and(less_than_pi, above_zero)
second_window = np.logical_and(~less_than_pi, ~above_zero)

plt.plot(x, y)
plt.scatter(drops[first_window,0],drops[first_window,1], c='C1')
plt.scatter(drops[second_window,0],drops[second_window,1], color='C2')


# In[17]:


first_set = np.logical_and(first_window, less_than_val)
second_set = np.logical_and(second_window, ~less_than_val)

plt.plot(x, y)
plt.scatter(drops[first_set,0],drops[first_set,1], c='C1')
plt.scatter(drops[second_set,0],drops[second_set,1], color='C2')


# In[18]:


I1 = len(drops[first_set])/len(drops[first_window])
print('proportion of window 1:', I1)

I2 = len(drops[second_set])/len(drops[second_window])
print('proportion of window 2:', I2)

print("proportion of total area (should be near zero):", I1-I2)


# In[19]:


def ComputeSine(ndrops):
    
    
    x = np.arange(0.0001, 2*np.pi, 0.0001)
    y = np.sin(x)

    drops = np.zeros([ndrops,2])

    for i in range(ndrops):

        xrand = random.random()*2*np.pi
        yrand = (random.random()-0.5)*2

        drops[i] = xrand,yrand

    less_than_pi = (drops[:,0] < np.pi) ##First half
    above_zero = (drops[:,1] > 0) ## Points below zero
    less_than_val = (drops[:,1] < np.sin(drops[:,0])) ## below positive curve

    first_window = np.logical_and(less_than_pi, above_zero)
    second_window = np.logical_and(~less_than_pi, ~above_zero)
    
    first_set = np.logical_and(first_window, less_than_val)
    second_set = np.logical_and(second_window, ~less_than_val)
    
    I1 = len(drops[first_set])/len(drops[first_window])
    I2 = len(drops[second_set])/len(drops[second_window])

    return I2-I1


# In[20]:


Nmin = 100 ## Had to be kind of big to make sure you get a random point in all four regions.
Nmax = 5000

estimates = np.zeros([Nmax,1])

for i in range(Nmin,Nmax):
    
    estimates[i] = ComputeSine(i)


# In[21]:


plt.figure(figsize=(8,8))
plt.plot(estimates)
plt.axis([0, N, -1, 1])
plt.grid()


# ## A Pathologically Terrible Integral
# 
# Consider the function below over the interval from 0 to 2.
# 
# $$y = \sin^2\left[\dfrac{1}{x(2-x)}\right]$$ 
# 
# Let's plot this son of gun.

# In[22]:


x = np.arange(0.00001,2,0.00001)
y = np.sin(1/(x*(2-x)))**2

plt.figure(figsize=(8,8))
plt.plot(x,y)
plt.axis([0, 2, 0, 1])
plt.grid()


# Let's zoom in on one of the wings, and we can see the problem. The integral varies wildly!

# In[23]:


x = np.arange(0.00001,2,0.00001)
y = np.sin(1/(x*(2-x)))**2

plt.figure(figsize=(8,8))
plt.plot(x,y)
plt.axis([1.75, 2, 0, 1])
plt.grid()


# ## Bring in Monte Carlo
# 
# Following the same approach estimate the value of the integral for this function and the uncertainty in your estimate.

# In[24]:


## your code here

