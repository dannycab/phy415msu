#!/usr/bin/env python
# coding: utf-8

# # 10 Nov 2022 - Applying the FFT to data
# 
# Y'all have learned the main process for using an FFT on a 1D signal, so let's use it in a scenario that would occur in a lab. You work in a lab that is observing light curves to determine if there are transiting objects near a star and, if so, what is their period. Using the brightness of the star itself, we can determine it's mass and then it's a quick analysis to get the mass of the transiting objects (Thanks, Newton!).
# 
# In this activity, you have three data files that describe the CCD voltage on a sensor as a function of time. The observations were taken over a 48 hour period. You will need to read in the data, determine the sampling frequency, and then develop an FFT model to look into the frequency components.
# 
# <img src="https://images.newscientist.com/wp-content/uploads/2019/09/26122246/c0471894-rejuvenated_gas_giant_planet_illustration-spl.jpg" width=600px>
# 
# ### Data Files
# 
# * [Observation 1](https://raw.githubusercontent.com/dannycab/phy415msu/main/MMIPbook/assets/data/FFT/obs1.csv)
# * [Observation 2](https://raw.githubusercontent.com/dannycab/phy415msu/main/MMIPbook/assets/data/FFT/obs2.csv)
# * [Observation 3](https://raw.githubusercontent.com/dannycab/phy415msu/main/MMIPbook/assets/data/FFT/obs3.csv)
# 
# The first data file is known to contain data from the observation of 2 transiting objects. Your lab mate misnamed the other two files, so it's not clear if they are the same set of observations or not.
# 
# Start with observation 1.

# ### Questions to answer
# 
# For observation 1,
# 
# 1. What does the FFT look like? Can you describe where the real observavtions might be in the plot?
# 2. Can you clean the noise from the data to find the real signal?
# 3. Can you estimate the transit times for the objects?
# 
# For observations 2 and 3,
# 
# 1. Which one (or both or neither) observations are those of observation 1?
# 2. If there's a file with new observations, can you learn the same things as above?

# 

# In[1]:


## your code here


# In[ ]:




