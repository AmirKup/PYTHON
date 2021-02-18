#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math
a = int(input("Введите число А = "))
b = int(input("Введите число Б = "))
y = math.sqrt(a**2+b**2)
p = y + a +b
print(p)

#4


# import math
# a = int(input("Введите число А = "))
# b = int(input("Введите число Б = "))
# g = math.sqrt(a*b)
# print(g)

# In[1]:


import math
x = int(input("Введите число X = "))
if x>=0:
    y = math.sqrt(x)
else:
    y = x**2 
print(x,y)       

#5


# In[7]:


import math
a = int(input("Введите число А = "))
b = int(input("Введите число Б = "))
c = int(input ("BBдите число С = "))
D = b**2-4*a*c
if D>=0:
    x1 = ((-b-math.sqrt(D))/2*a)
    x2 = ((-b+math.sqrt(D))/2*a)
    print(x1,x2)
else:
    print("Решение НЕТ")
    
#6


# In[8]:


x = int(input("Введите число X = "))
y = int(input("Введите число Y = "))
if x==0:
    print("ERROR")
else:
    z = y/x
    print(x,y,z)
    
#7


# In[9]:


a = int(input("Введите число А = "))
b = int(input("Введите число Б = "))
s = a*b
if s>500:
    s= s+0,9
else:
    print(s)
    
#8


# In[1]:


a = int(input("Введите число А = "))
b = int(input("Введите число Б = "))
if a == b:
    print(a)
else:
    if a> b:
        a = a-b
    else:
        b = b - a

#9


# In[2]:


n = int(input("Введите число n = "))
S = 0
i = 1
if i <= n:
    S = S + i
    i = i + 2
else:
    print(S)
    
#10


# In[3]:


Q = int(input("Введите число Q = "))
S = 0
i = 1
if S>Q:
    S = S + i
    i = i + 1
else:
    print(i-2)
    
    
#12


# In[3]:


import math
a = int(input("Введите число А = "))
b = int(input("Введите число Б = "))
c = int(input ("BBдите число С = "))
D = b**2-4*a*c
if D >= 0:
    x1 = (-b-math.sqrt(D))/(2*a)
    x2 = (-b+math.sqrt(D))/(2*a)
    print(x1,x2)
else:
    print("ERROR")
    
#6


# In[5]:


n = 3
i = 1
S = 0
if i<=n:
    i = i + 1
    S = S + (3*i+2)
else: 
    print("END")
    
#13


# In[8]:


x = int(input("Введите число X = "))
if x<0:
    y = x**2+1
else:
    if x>=1:
        y = 4x-1
    else:
        y = 2x+1
print(y)

#14


# In[10]:


a = int(input("Введите число A = "))
if a == 0:
    x = 2
else:
    if a>0:
        x<c
    else:
        x>c
print(x)

#15


# In[11]:


import math
a = int(input("Введите число А = "))
b = int(input("Введите число Б = "))
if a == 0:
    if b == 0:
        x = 2
    else:
        print("ERROR")
else:
    c = b/a
    if  a> 0:
        x>c
    else:
        x<c
print(x)

#17


# In[12]:


import math
a = int(input("Введите число А = "))
b = int(input("Введите число Б = "))
c = int(input ("BBдите число С = "))
min = a
if min >b:
    min = b
elif min >c:
    min = c
print(min)

#18


# In[ ]:


import math
ST = int(input("Введите число ST = "))

