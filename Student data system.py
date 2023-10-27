#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def studentdata():
    d={}
    while True:
        studentid=input("enter the student id :")
        studentMarks=input("enter the student marks seperated by comma :")
        reply=input("enter 'no' if there are no more students :")
        d[studentid]=studentMarks.split(",")
        if (reply=="no"):
            return d
            break
        else:
            continue
def avg(d):
    d1={}
    for x in d:
        l=d[x]
        s=0
        for y in l:
            s+= int(y)
        d1[x]=s/len(l)
    return d1       
y=studentdata()
list=avg(y)
print(list)

