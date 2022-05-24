#!/usr/bin/env python
# coding: utf-8

# ![Blue%20&%20White%20Modern%20Tutorial%20Youtube%20Thumbnail.png](attachment:Blue%20&%20White%20Modern%20Tutorial%20Youtube%20Thumbnail.png)

# # Module
# 1. A module is a collection of functions, variables, and classes saved in a single file.
# 2. Every Python (.py) file can be served as a module.

# In[1]:


#data1 = "Module"
#data2 = 3.14
#def add(x,y): 
#    print("The Sum:",x+y)
    
#def product(x,y): 
#    print("The Product:",x*y)


# In[2]:


import myModule


# In[3]:


print(myModule.data1)
print(myModule.data2)
myModule.add(10,7)
myModule.product(10,22)
#add(10,2)
#print(myModule.data3)


# # Module renaming

# In[4]:


import myModule as ta # ta is a alias name


# In[5]:


print(ta.data1)
print(ta.data2)
ta.add(4,20)
ta.product(8,20)
#print(data1)
#print(myModule.data2)
#myModule.add(10,2)


# # from ... import
# We don't need the module name to access the members (both data and function).

# In[6]:


from myModule import data1, product
#from M2 import data1

print(data1)
#print(data2)
#print(data2)
product(3,5)
#add(3,5)


# # Import all members of a module 
# 

# In[7]:


from myModule import *
print(data1)
print(data2)
product(13,5)
add(13,51)


# # Various possibilties of import
# * import module_name 
# * import module_x, module_y, module_z 
# * import module_name as ac 
# * import module_name1 as m1, module_name2 as m2, module_name3 # member aliasing
# 
# * from module import member 
# * from module import member_1, member_2, memebr_3 
# * from module import memeber_1 as myName 
# * from module import *

# In[8]:


from myModule import data1, add
print("Data1 is: ",data1)
add(17, 19)


# # Finding number of modules, functions, and variables

# In[9]:


print(dir())


# In[10]:


import myModule
print(dir(myModule))


# # The Special variable \__name\__
# * A specific variable called “\__name\__”  is introduced to every Python application.
# 
# * Here, "\__name\__"  variable holds information about whether the program is run as a standalone program or as a module. In other words, "\__name\__" variable tells us whether the program was run directly or as a module.
# 
# * If the program was run as a standalone program, the value of this variable would be"\__main\__", otherwise the value of this variable is the name of the module where it is declared if the program is run as a module from another program.
# 

# In[1]:


"""
File A
"""
print ("File_A  __name__ = %s" %__name__) 
  
if __name__ == "__main__": 
    print ("File_A is being run directly")
else: 
    print ("File_A is being imported")


# In[26]:


import fileA


# In[2]:


"""
File B
"""

import fileA
  
print ("File_B __name__ = %s" %__name__) 

 
if __name__ == "__main__": 
    print ("File_B is being run directly")
else: 
    print ("File_B is being imported")


# # List of all built in modules

# In[13]:


#help ('modules') # list of all available modules


# In[14]:


#from random import *
#from math import *
#from datetime import *


# In[15]:


# Example 2: of random module
from random import * 
for i in range(2): 
    print("\nPrint random(): ",random()) # Integer random values within the range 0<x<1
    print("Print randint(): ",randint(1,10)) # Integer random values within the range 1 <=x<= 10
    print("Print uniform",uniform(1,10)) # Floating random values within the range 1 <x<10


# # The choice() function
# It returns a random element from the given sequence (list or tuple).

# In[16]:


from random import * 
list=["red","green","blue","orange","black"] 
for i in range(3): 
    print(choice(list))


# In[17]:


# Example of choices()
import random
mylist = ["Red", "Green", "Blue"]
print(random.choices(mylist, weights = [2, 1, 10], k = 7))


# # Shuffling a list

# In[18]:


# Example of list shuffling
import random
myList = ["A", "B", "C", "D", "E", "F"]
  
print("Original list is: ", myList)

random.shuffle(myList)
print("After shuffle: ", myList)

random.shuffle(myList)
print("After shuffle: ", myList)


# # Math module

# In[19]:


from math import *
print("The square root is: ",sqrt(7))
print("The factorial is: ",factorial(7))


# In[20]:


#help('math')

