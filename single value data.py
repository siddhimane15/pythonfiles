Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#single value data type
#-->we can pass only one one value
#INT DATA TYPE-->
a=100
a
100
type(a)
<class 'int'>
b=-78
b
-78
type(b)
<class 'int'>
int()
0
s=int(100)
s
100
type(s)
<class 'int'>

s1=int(-500)
s1
-500
type(s1)
<class 'int'>

s2=int(12.345)
s2
12
s2=complex(12.345)
s2
(12.345+0j)

c=-56.78
c
-56.78
type(c)
<class 'float'>
float()
0.0
complex()
0j
float(15)
15.0
int(90.56)
90

#complex-->combination of real number and imaginary number
#-->a+bj,a-bj
#--->in th place of j----J/j
#real--->int,float,+ve,-ve   imaginary---->int,float,+ve,-ve
#j===constant

a=10+5.5j
a
(10+5.5j)
c=12+5j
c
(12+5j)
d=45-12J
d
(45-12j)

e=23+12i
SyntaxError: invalid decimal literal

#real part feching----> var_name.real
#imaginary part fechng--->var_name.imaginary
d=45-10j
d.real()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    d.real()
TypeError: 'float' object is not callable
d
(45-10j)
d.real
45.0
d.imag
-10.0
s=complex(10,20)
s
(10+20j)
s1=complex(-100,-200)
s1
(-100-200j)
>>> s1.real
-100.0
>>> s1.imag
-200.0
>>> 
>>> 
>>> True+True
2
>>> 
>>> False+False
0
>>> #True--->1  Flase--->0
>>> #internally boolean data type we can representas object---->bool()
>>> bool()
False
>>> #syntax:var_name=bool(element)
>>> x=bool(100)
>>> x
True
>>> y=bool("Hii")
>>> y
True
>>> z=bool(5.6)
>>> z
True
>>> a=bool(15+8j)
>>> a
True
>>> r=bool(0)
>>> r
False
>>> r1=bool(True)
>>> r1
True
