Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=[10,15,20,25]
b=a.copy()
a
[10, 15, 20, 25]
b
[10, 15, 20, 25]
id(a)
1641988766784
id(b)
1641988656832
#Modification in a variable
a
[10, 15, 20, 25]
a[0]="Hii"
#var_name[position]=value
a
['Hii', 15, 20, 25]
b
[10, 15, 20, 25]


e=["a","b","c","d"]
w=e.copy()
e
['a', 'b', 'c', 'd']
w
['a', 'b', 'c', 'd']
id(e)
1641943780288
id(w)
1641988755200
w[1]="Hello"
w
['a', 'Hello', 'c', 'd']
w.append(10)
w
['a', 'Hello', 'c', 'd', 10]
['a', 'Hello', 'c', 'd', 10]
['a', 'Hello', 'c', 'd', 10]
KeyboardInterrupt

#nested list ex
#nested list-->list inside another list
m=[100,200,300,["a","b","c"]]
n=m.copy()
m
[100, 200, 300, ['a', 'b', 'c']]
n
[100, 200, 300, ['a', 'b', 'c']]
#complete list id address
id(m)
1641988772160
id(n)
1641988655872

#nested list id adress : --> id(var_name[position])
m=
SyntaxError: invalid syntax
m
[100, 200, 300, ['a', 'b', 'c']]
[100, 200, 300, ['a', 'b', 'c']]
KeyboardInterrupt
m[3]
['a', 'b', 'c']
id(m[3])
1641988656512
id(n[3])
1641988656512
#modifictaion in m variable outside the nested list
m
[100, 200, 300, ['a', 'b', 'c']]
m[1]
200
m[1]=500
m
[100, 500, 300, ['a', 'b', 'c']]
n
[100, 200, 300, ['a', 'b', 'c']]

#modification in n variable outside the nested list
n
[100, 200, 300, ['a', 'b', 'c']]
n[0]=
SyntaxError: invalid syntax
n[0]="python"
n
['python', 200, 300, ['a', 'b', 'c']]
m
[100, 500, 300, ['a', 'b', 'c']]
#modification in m variable inside nested list
m
[100, 500, 300, ['a', 'b', 'c']]
m[3]
['a', 'b', 'c']
m[3][0]
'a'
m[3][0]=10
m
[100, 500, 300, [10, 'b', 'c']]
n
['python', 200, 300, [10, 'b', 'c']]
n[3][2]=700
n
['python', 200, 300, [10, 'b', 700]]
m
[100, 500, 300, [10, 'b', 700]]
v=[1,2,3,[900,800,700,600]]
u=v.copy()
u
[1, 2, 3, [900, 800, 700, 600]]
v
[1, 2, 3, [900, 800, 700, 600]]
id(u)
1641988817408
id(v)
1641988656576
id(u[3])
1641987456256
id(v[3])
1641987456256

#modification in v variable
v
[1, 2, 3, [900, 800, 700, 600]]
v[0]=100
v
[100, 2, 3, [900, 800, 700, 600]]
u[0]
1
u[1]=100
u
[1, 100, 3, [900, 800, 700, 600]]
u[2]=400
u
[1, 100, 400, [900, 800, 700, 600]]
v
[100, 2, 3, [900, 800, 700, 600]]
#modification in v variable inside the nested list
v
[100, 2, 3, [900, 800, 700, 600]]
v[1][0]="joy"
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    v[1][0]="joy"
TypeError: 'int' object does not support item assignment
v[3][0]="joy"
v
[100, 2, 3, ['joy', 800, 700, 600]]
u
[1, 100, 400, ['joy', 800, 700, 600]]
#modification in u vafriable
u[1][3]="think"
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    u[1][3]="think"
TypeError: 'int' object does not support item assignment
u[3][3]="think"
u
[1, 100, 400, ['joy', 800, 700, 'think']]
v
[100, 2, 3, ['joy', 800, 700, 'think']]

#deepcopy()
#step 1:from copy import deepcopy
#syntax: new_var=deepcopy(old var_name)

from copy import deepcopy
a=[1,2,3,4,5,90]
a
[1, 2, 3, 4, 5, 90]
b=deepcopy(a)
b
[1, 2, 3, 4, 5, 90]
id(a)
1641948342080
id(b)
1641988766784

#nested list data in deepcopy

c=[11,12,13,14,[1,2,3,4]]
d=deepcopy(c)
c
[11, 12, 13, 14, [1, 2, 3, 4]]
d
[11, 12, 13, 14, [1, 2, 3, 4]]
id(c)
1641988782336
id(d)
1641988824192
id(c[4])
1641988824512
id(d[4])
1641988820672


#ASCII VAULES:American Standard Code information interchange
#2 format:1] ord() -->ordinal -->accept single characater in quote output as number
        #2] char()-->characater-->accept number & ouput is character
#sytax:   ord('char')    chr(number)

ord("A")
65
ORD("Z")
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    ORD("Z")
NameError: name 'ORD' is not defined. Did you mean: 'ord'?
ord("Z")
90
ord("a")
97
ord("Z")
90
ord("z")
122


ord("1")
49
ord("9")
57

ord("abc")
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    ord("abc")
TypeError: ord() expected a character, but string of length 3 found
#ord always accept single signle value

ord("A")
65
>>> chr(65)
'A'
>>> 
>>> ord("z")
122
>>> chr(122)
'z'
>>> 
>>> 
>>> #sort():
>>> #Accept only homogeneous data
>>> #syntax:1. var_name.sort()
>>> #2.var_name.sort(reverse=False)
>>> #3.var_name.sort(reverse=True)
>>> #by default 1&2 syntax is ascending - decending   -->lower to bigger
>>> #by defualt 3 syntax -->decending to ascending -->bigger to lower
>>> d=[12,6,3,120,0.5,1,2,90,1000,7]
>>> d.sort()
>>> d
[0.5, 1, 2, 3, 6, 7, 12, 90, 120, 1000]
>>> d.sort(reverse=False)
>>> d
[0.5, 1, 2, 3, 6, 7, 12, 90, 120, 1000]
>>> d.sort(reverse=True)
>>> d
[1000, 120, 90, 12, 7, 6, 3, 2, 1, 0.5]
>>> 
>>> 
>>> 
>>> #unpacking(*)
>>> a=[1,2,3,4,5]
>>> b=["a","b"]
>>> print(*a)
1 2 3 4 5
>>> print(*b)
a b
>>> u=[*a,*b]
>>> u
[1, 2, 3, 4, 5, 'a', 'b']
