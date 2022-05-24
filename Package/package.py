#!/usr/bin/env python
# coding: utf-8

# ![Package.png](attachment:Package.png)

# # Packages
# 1. It is a technique for encapsulating related modules into a single entity.
# 
# 2. A package is a folder or directory that contains a collection of Python modules.
# 
# 3. A Python package is any folder or directory that contains the \__init\__.py file and the \__init\__.py file can be left blank. 
# 
# 4. A package can also have sub-packages.
# 
# 5. \__init\__.py helps the Python interpreter to recognise the folder as package. 

# # Popular python packages
# * **NumPy**:tool for scientific computing  
# * **pandas**: File load and save. Reshaping, pivoting, slicing, indexing, subsetting, aggregating, transforming, merging and joining datasets. 
# * **Matplotlib**: For data exploration and visualization library.
# * **Seaborn**: Seaborn is a high-level interface that allows us to create great statistical plots using only a few lines of code.
# * **scikit-learn**: Tool for data analysis and prediction.
# * **Requests**: Tool to make HTTP requests more responsive and user friendly.  
# * **urllib3**:user-friendly HTTP client
# * **NLTK**: Natural Language Toolkit is a toll for language data processing.
# * **Pillow**: tool for image manipulation
# * **pytest**: for software testing (e.g., usint test)

# In[30]:


# Example 
import numpy as ac
import pandas as ac

A = numpy.array([[1,2,3],
             [9,7,6]])
print("The array is: \n",A)


# # How to make a package
# * Make a package called *myPackage* that contains two modules: *module_A* and *module_B*. 
#     
# # Steps to create a package
# 1. Create a new folder called myPackage.
# 2. Create an empty Python file called \__init\__.py inside this folder.
# 3. Create two modules in this subdirectory, module_A and module_B.

# ![packagePhoto-2.jpg](attachment:packagePhoto-2.jpg)

# In[34]:


from myPackage.module_A import *
from myPackage.module_B import *
#print(display())

output1 = addition(3,89)
print("The output 1 is: ",output1)

output2 = product(6,71)
print("The output 2 is: ",output2)


# # Importing a complete package

# In[17]:


from numpy import *


# In[36]:


import numpy
#help(numpy) # To get detail information


# # To know list of installed packages

# In[39]:


#!pip list
#!pip freeze


# In[ ]:


# !pip list -o 


# # To upgrade package

# In[40]:


get_ipython().system('pip install -U numpy, pasdas')


# # Import more than one packages

# In[41]:


import numpy, pandas, os


# # Display version of a package

# In[42]:


print(numpy.__version__) # print(packageName.__version__)


# In[43]:


print(pandas.__version__)


# ![WhatsApp%20Image%202022-01-17%20at%207.01.51%20PM.jpeg](attachment:WhatsApp%20Image%202022-01-17%20at%207.01.51%20PM.jpeg)

# In[ ]:




