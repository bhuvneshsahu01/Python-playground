#!/usr/bin/env python
# coding: utf-8

# # Encoder Decoder

# In[ ]:


import numpy as np
q1=input("what do you want to do\n press 1 to encode\t press 2 to decode")
if (q1=="1"):
    fs=[]
    s1=input("give a sentence to encode")
    s2=["qwertyuioplkjhgfdsazxcvbnm"]
    p=0
    for i in s1:
        i=np.random.permutation(np.arange(0,25))
        i=i[0:3]
        s3=[]
        for j in range (0,3):
            t=i[j]
            x=s2[0][t]
            s3.append(x)
        s5=s3[0]+s3[1]+s3[2]
        fs.append(s1[p]+s5)
        p=p+1
    print(str(fs))
elif(q1=="2"):
    s1=input("give a sentence to decode")
s1=s1.split(", ")
fd=[]
for i in s1:
    fd.append(i[1])
fd1='' .join([str(item) for item in fd])
print(fd1)
 


# In[ ]:


import numpy as np
q1=input("what do you want to do\n press 1 to encode\t press 2 to decode")
if (q1=="1"):
    fs=[]
    fsrf=[]
    s1=input("give a sentence to encode\n")
    s2=["qwertyuioplkjhgfdsazxcvbnm"]
    p=0
    g=0
    final=[]
    for i in s1:
        i=np.random.permutation(np.arange(0,25))
        i=i[0:3]
        s3=[]
        for j in range (0,3):
            t=i[j]
            x=s2[0][t]
            s3.append(x)
        s5=s3[0]+s3[1]+s3[2]
        fs.append(s1[p]+s5)
        p=p+1
    for i in fs:
        i=np.random.permutation(np.arange(0,25))
        i=i[0:2]
        s3=[]
        for j in range (0,2):
            t=i[j]
            x=s2[0][t]
            s3.append(x)
        s5=s3[0]+s3[1]
        fsrf.append(s5+fs[g])
        g=g+1
    for i in fsrf:
        q=i[2:6]
        q=q.strip()
        e=i[0:2]+q
        final.append(e)
    print(final)
elif(q1=="2"):
    s1=input("give a sentence to decode")
    s1=s1.split(", ")
    fd=[]
    for i in s1:
        if (len(i)%2==0):
            fd.append(i[3])
        else:
            fd.append(" ")
    fd1='' .join([str(item) for item in fd])
    print(fd1)

    
    
    
    

