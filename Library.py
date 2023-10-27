#!/usr/bin/env python
# coding: utf-8

# In[ ]:


book_name=[]
genre=[]
author=[]
location=[]
x=int(input("what do want to do : \n1) add a book\n2) find a book "))
if x==1:
    a=input("book name ")
    b=input("genre ")
    c=input("author ")
    d=input("location ")
    book_name.append(a.lower())
    genre.append(b.lower())
    author.append(c.lower())
    location.append(d.lower())
    print("book information is saved")
elif x==2:
    y=int(input("what do you want to use as search filter : \n1) by book name \n2) by genre \n3) by author"))
    if y==1:
        n=input("enter book name :")
        for i in range(len(genre)):
            if book_name[i]==n.lower():
                idx=i
    if y==2:
        n=input("enter genre :")
        for i in range(len(genre)):
            if genre[i]==n.lower():
                idx=i
    if y==3:
        n=input("enter author :")
        for i in range(len(genre)):
            if author[i]==n.lower():
                idx=i  
    print(f"name of the book is {book_name[idx]} \ngenre is {genre[idx]} \nauthor is {author[idx]}") 
d=input("do you want to continue : \n1) yes \n2) no")
if d==1:
    continue    
   
            

