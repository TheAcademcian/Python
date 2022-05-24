"""
File A
"""
print ("File_A  __name__ = %s" %__name__) 
  
if __name__ == "__main__": 
    print ("File_A is being run directly")
else: 
    print ("File_A is being imported")