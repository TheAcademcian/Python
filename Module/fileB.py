# -*- coding: utf-8 -*-
"""
File B
"""
import fileA
 
print ("File_B __name__ = %s" %__name__) 
  
if __name__ == "__main__": 
    print ("File_B is being run directly")
else: 
    print ("File_B is being imported")