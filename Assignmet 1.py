#!/usr/bin/env python
# coding: utf-8

# 2.Write a program which will find all such numbers which are divisible by 7 but are not a multiple
# of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
# comma-separated sequence on a single line.

# In[1]:


numbers=[]
for n in range(2000, 3200):
    if (n%7==0) and (n%5!=0):
        numbers.append(str(n))
print (','.join(numbers))


# 3.Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name. 
# 

# In[12]:


FirstName=input('Enter your First Name:')


# In[2]:


Lastname=input('Enter your Last Name:')


# In[7]:


print(FirstName)


# In[11]:


print(Lastname+" "+FirstName)


# 4.Write a Python program to find the volume of a sphere with diameter 12 cm.  
#  
# Formula: V=4/3 * π * r 3 

# In[13]:


V=4/3*3.14*6**3


# In[15]:


print(V)


# # Task 2

# 1.Write a program which accepts a sequence of comma-separated numbers from console and generate a list. 

# In[16]:


numbers=input('Enter a sequence of comma-sepated numbers:')


# In[17]:


list=numbers.split(",")


# In[18]:


print(list)


# 2.Create the below pattern using nested for loop in Python. 
#  
#  
# *  
# * *
# * * *
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * *
# * 

# In[22]:


rows = 5
for i in range (0, rows):
  for j in range(0, i + 1):
     print("* ", end='')
  print(" ")
for i in range (rows, 0, -1):
  for j in range(0, i -1):
     print("* ", end='')
  print(" ")


# 3.  
#  
# Write a Python program to reverse a word after accepting the input from the user. 
#  
# Sample Output: 
#  
# Input word: AcadGild 
#  
# Output: dilGdacA 

# In[23]:


Word=input('Enter a word:')


# In[24]:


ReversedWord=Word[::-1]


# In[26]:


print(ReversedWord)


# 4.  
#  Write a Python Program to print the given string in the format specified in the ​sample output. 
#  WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens 
#  
# Sample Output: 
#  
# WE, THE PEOPLE OF INDIA,
#         having solemnly resolved to constitute India into a SOVEREIGN, !
#                SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
#                and to secure to all its citizens 

# In[30]:


string = "WE, THE PEOPLE OF INDIA,{}having solemnly resolved to constitute India into a SOVEREIGN,{}SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC{}and to secure to all its citizens{}"
print(string.format('\n\t','!\n\t\t','\n\t\t',':'))


# In[ ]:




