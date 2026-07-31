Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#set
#union-->var_name1.union(var_name2)1.original var,2.reference var
x={1,2,3,,4}
SyntaxError: invalid syntax
x={1,2,3,4}
y={"a","b","c"}
x.union(y)
{1, 2, 3, 4, 'c', 'b', 'a'}
y.union(x)
{'c', 1, 2, 3, 4, 'b', 'a'}
x|y
{1, 2, 3, 4, 'c', 'b', 'a'}
d={"python","enter",78.90}
e={True,False,3+4j,"set"}
e.union(d)
{False, True, 'enter', 'set', 'python', 78.9, (3+4j)}
d|e
{'enter', False, True, 'set', 'python', 78.9, (3+4j)}


#intersection()---->set1.intersection(set2)

#set1--->original set
#set2---->refernce set/specified set
x={12,800,True,78,10}
y={800,True,10,98,67}
x.intersection(y)
{800, True, 10}
y.intersection (x)
{800, True, 10}
d.intersection(e)
set()

#symmetric_difference--->set1.symmetric_difference(Set2)
x
{800, True, 10, 12, 78}
y
{800, True, 98, 67, 10}
x.intersection(y)
{800, True, 10}
x.symmetric_difference(y)
{98, 67, 12, 78}


u={11,12,13,14,15}
t={11,12,13,14,15}
u.symmetric_difference(t)
set()

d={12,78.9,True}
e={False,"Set",(3+4j)}
d.symmetric_difference(e)
{False, True, 'Set', 12, 78.9, (3+4j)}


#difference--->set1.difference.(set2)
x={"A","B","C?,90,100,45}
   
SyntaxError: unterminated string literal (detected at line 1)
x={"A","B","C",90,100,45}
   
y={"D","E","A",56.78,5+4j}
   
x.difference.(y)
   
SyntaxError: invalid syntax
x.difference(y)
   
{100, 45, 'B', 90, 'C'}
y.difference(x)
   
{56.78, (5+4j), 'E', 'D'}

k={"chat","kit","cat","bat","mat",
   "web","snap"}
   
l={"Mat","kit","sql","chat,"enter"}
   
SyntaxError: unterminated string literal (detected at line 1)
l={"Mat","kit","sql","chat}
   
SyntaxError: unterminated string literal (detected at line 1)
l={"Mat","kit","sql","chat}
   
SyntaxError: unterminated string literal (detected at line 1)
l={"Mat","kit","sql","chat,"enter"}
   
SyntaxError: unterminated string literal (detected at line 1)
l={"Mat","kit","sql","chat","enter"}
   
k.difference(l)
   
{'cat', 'bat', 'snap', 'mat', 'web'}
l.difference(k)
   
{'enter', 'sql', 'Mat'}


#boolean methods----->3
   
#isuperset-->var_name1.issuperset(var_name2)
   
#issunset-->var_name1.issubset(var_name2)
   
#isdisjoint--->var_name1.disjoint(var_name2)
   

x={100,200,300,400,500)
   
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
x={100,200,300,400,500}
   
y={500,100,300,200}
   
x.issuperset(y)
   
True
y.issuperset(x)
   
False
False
   
False


d={"A","B","C","E",999,888,777}
   
e={"F","G","A","B","C","D","E",999,888,777}
   
d.issuperset(e)
   
False
e.issuperset(d}
   
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
e.issuperset(d)
   
True

#issubset()
   
d.issubset(e)
   
True
e.issubset(d)
   
False
#isdisjoint()
   
a={1,2,3,4,5}
   
b={7,8,9,10}
   
a.isdisjoint(b)
   
True
a
   
{1, 2, 3, 4, 5}
c={1,2,78,90}
   
a.isdisjoint(c)
   
False
c.isdisjoint(a)
   
False
dir(set)
   
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
#typecasting--->the process of converting one data type to another data type.
   
#default value of collection data type
   
str()
   
''
tuple()
   
()
list()
   
[]
set()
   
set()
dict()
   
{}
a="Python"
   
type("python")
   
<class 'str'>
list(a)
   
['P', 'y', 't', 'h', 'o', 'n']
list("python")
   
['p', 'y', 't', 'h', 'o', 'n']
tuple(a)
   
('P', 'y', 't', 'h', 'o', 'n')
set(a)
   
{'h', 'y', 'n', 't', 'P', 'o'}
dict(a)
   
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    dict(a)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
m="evening"
   
a=list(m)
   
a
   
['e', 'v', 'e', 'n', 'i', 'n', 'g']
m
   
'evening'
type(a)
   
<class 'list'>
type(m)
   
<class 'str'>


l=[10,20,30]
   
str(l)
   
'[10, 20, 30]'
list(l)
   
[10, 20, 30]
tuple(l)
   
(10, 20, 30)
set(l)
   
{10, 20, 30}
dict(l)
   
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    dict(l)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
y={100,200,500,78,99,1}
   
str(y)
   
'{1, 99, 100, 500, 200, 78}'
list(y)
   
[1, 99, 100, 500, 200, 78]
tuple(y)
   
(1, 99, 100, 500, 200, 78)
set(y)
   
{1, 99, 100, 500, 200, 78}
dict(y)
   
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    dict(y)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
w={12:89,"abc":11,99:80}
   
str(w)
   
"{12: 89, 'abc': 11, 99: 80}"
list(w)
   
[12, 'abc', 99]
tuple(w)
   
(12, 'abc', 99)
>>> set(w)
...    
{99, 12, 'abc'}
>>> 
>>> 
>>> 

... 
... 
>>> 

>>> 

... 
... 
>>> 

>>> 

... 
... 
>>> 
>>> 

... 
... 
>>> 

>>> 

... 
>>> 

>>> 

