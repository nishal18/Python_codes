#!/usr/bin/env python
# coding: utf-8

# In[42]:


import math
strong=[]
    
def digfun(n):
    temp=n
    sum=0
    while(n!=0):
        dig=n%10
        sum=sum+math.factorial(dig)
        n=n//10
    if (sum==temp):
        strong.append("yes")
    else:
        strong.append("no")

def fact(f):
    fa=1
    for i in range(1,f+1):
        fa=fa*1
    return fa


# In[43]:


input_array=[145,375,100,2,10]
for i in (input_array):
    digfun(i)


# In[44]:


strong


# In[ ]:




