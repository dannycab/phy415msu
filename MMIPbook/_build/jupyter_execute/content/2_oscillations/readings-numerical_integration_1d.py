#!/usr/bin/env python
# coding: utf-8

# # 2 - Numerical Integration in 1D
# 
# Principal Ideas for this unit will come from [Newman Chapter 8, Section 1](https://github.com/dannycab/phy415msu/blob/main/MMIPbook/assets/pdfs/scans/Newman_Ch8_ODEs.pdf), which is the reading assigned below.
# 
# 
# We have seen how we can quickly exhaust our analytical tools when we investigate systems with interesting and complex behavior. We can see much from the perspective of phase space in terms of the qualitatively different behaviors (e.g., oscillations vs rotations, both clockwise and counter-clockwise, in the large angle pendulum). But what if we want to find the specific trajectory of a given set of initial conditions.
# 
# That is we want to be able to take a more general differential equation:
# 
# $$\ddot{x} = f(x,\dot{x},t)$$
# 
# to a solution for all (or some specified amount)of time, $x(t)$...in (most) cases...because sometimes integrals don't converge.
# 
# We can use **numerical integration** to find these trajectories. Below is a video describing 3 coupled ODEs, the [Lorenz equations](https://en.wikipedia.org/wiki/Lorenz_system), that are quite famous. You will be able to model systems like this, but for now think of it as motivation for why we want to learn numerical integration.

# In[1]:


from IPython.display import YouTubeVideo
YouTubeVideo("aAJkLh76QnM", 800, 600)


# ## Nonlinear Science
# 
# Some of the most interesting ODEs to work with are those that lead to chaos, have interesting behaviors in different parts of phase space, are highly sensitive to initial conditions, or that have complex bound orbits (in real or phase space). This area of study in physics overlaps with a broad interdisciplinary field called [Nonlinear Science](https://en.wikipedia.org/wiki/Nonlinear_system), which studies all manner of systems where the results are not simply proportional to the input features. This work includes theory, applied science, and experimental work. As it is difficult to find truly linear systems in the real world, nonlinear science is quite interdisciplinary with physics research in the areas of [magnetohydrodynamics](https://complex.umd.edu/research/MHD_dynamos/MHD_dynamos.php), [fluid mechanics](), [bio-inspired design](https://meche.mit.edu/people/faculty/PEKO@MIT.EDU), [biophysics (cellular)](https://curtisresearch.gatech.edu/index.php), [biophysics (animal locomotion)](https://crablab.gatech.edu/), [atomic and molecular physics](https://jila.colorado.edu/lewandowski), and many more fields.
# 
# We will focus on integrating 1 dimensional ODEs (that is, ODEs of only one variable like the SHO). To that end the reding this week aims to inform you with the simplest of the integrators the [Euler-Cromer integration](https://en.wikipedia.org/wiki/Semi-implicit_Euler_method) technique. This approach is intuitive, straight-forward, and forms the basis for better and far more accurate methods like [Runge-Kutta](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods). 
# 
# Through this week's activities, we will introduce several integration methods, but you will learn to use the [built-in integrator](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html?highlight=odeint) (```odeint```) from scipy, which are more efficient than what we could write ourselves.
# 
# 
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

# 
