#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
x=[]
k=0
for i in range(1000):
    while True:
        if random.choice(["tail","head"])=="tail":
        
            k+=1
        else:
            x.append(k)
            k=0
            break
print(x)

import random
x=[]
k=0
for i in range(1000):
    while True:
        if random.choice(["tail","head"])=="head":
            k+=1
        else:
            x.append(k)
            k=0
            break
print(x)         

