#!/usr/bin/env python
# coding: utf-8

# In[8]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# ## Uniform distribution

# In[9]:


#uniform distribution
values = np.random.uniform(-10,10,100000)
# -10 to +10 will the range and 100000 are number of data points 
plt.hist(values,50)
#histogram with 50 bins
plt.show()


# ## Normal/Gussian

# In[17]:


from scipy.stats import norm
x = np.arange(-3, 3, 0.1)
plt.plot(x,norm.pdf(x))
#plots a normal distribution graph between -3 and +3


# Generate some random numbers with a normal distribution. "mu" is the desired mean, "sigma" is the standard deviation

# In[19]:


mu =5.0
sigma = 0.2
values =np.random.normal(mu, sigma, 1000)
plt.hist(values, 50)
#50 buckets
plt.show()


# ## expontential PDF/ "Power law"

# In[21]:


from scipy.stats import expon
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.001)
plt.plot(x, expon.pdf(x))


# In[24]:


from scipy.stats import binom

n,p =10, 0.5
x = np.arange(0, 10, 0.001)
plt.plot(x, binom.pmf(x,n,p))


# Example: My website gets on average 500 visits per day. What's the odds of getting 550?
# 

# ## Poission Probability Mass Function

# In[23]:



from scipy.stats import poisson
import matplotlib.pyplot as plt

mu = 500
x = np.arange(400, 600, 0.5)
plt.plot(x, poisson.pmf(x, mu))


# In[ ]:




