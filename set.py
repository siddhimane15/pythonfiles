Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#set:   1]unique element
       # 2]won't accept duplicate elements
       
        #3]unorder data type
       
        #4]MUtable data type
       
#       5]syntax: var_name{ele1,ele2,ele3....}
#not support indexing,slicing
#set not create by normal  way  only create by object set()
#only pass immutable and single value data otherwise unhashable type of error.
a=
SyntaxError: invalid syntax
a={}
type(a)
<class 'dict'>
x=(1,2.4,False,5+4j,"hii",(1,2,3))
x
(1, 2.4, False, (5+4j), 'hii', (1, 2, 3))
x={1,2.4,False,5+4j,"hii",(1,2,3)}
x
{False, 1, 2.4, (5+4j), 'hii', (1, 2, 3)}
x={1,2.4,False,5+4j,"hii",(1,2,3),[12,45,67}
   
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
x={1,2.4,False,5+4j,"hii",(1,2,3),[12,45,67]}
   
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    x={1,2.4,False,5+4j,"hii",(1,2,3),[12,45,67]}
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
x[0]
   
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    x[0]
TypeError: 'set' object is not subscriptable
dir(set)
   
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
# 1] adding element into the set data type
   
#add()-->var_name.add(element)
   
s={}
   
s.add(10)
   
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s.add(10)
AttributeError: 'dict' object has no attribute 'add'
s.add({10})
   
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s.add({10})
AttributeError: 'dict' object has no attribute 'add'
a={1}
   
a
   
{1}
type(a)
   
<class 'set'>
c=set()
   
c
   
set()
c.add(10)
   
c
   
{10}
c.add(7.2)
   
c
   
{10, 7.2}
c.add(3.4j)
   

c
   
{3.4j, 10, 7.2}
c.add(True)
   
c
   
{3.4j, 10, True, 7.2}
c.add("sql")
   
c
   
{True, 7.2, 3.4j, 10, 'sql'}
c.add((23,45,67))
   
c
   
{True, 7.2, 3.4j, 10, (23, 45, 67), 'sql'}
c.add([12,45,67,89])
   
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    c.add([12,45,67,89])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
c.add(10)
   
c
   
{True, 7.2, 3.4j, 10, (23, 45, 67), 'sql'}
c.add({34:67})
   
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    c.add({34:67})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
c.add({23,45,67})
   
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    c.add({23,45,67})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
c.add()
   
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    c.add()
TypeError: set.add() takes exactly one argument (0 given)
c.add(100,900,"bye")
   
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    c.add(100,900,"bye")
TypeError: set.add() takes exactly one argument (3 given)
c.add((100,900,"bye"))
   
c
   
{True, (100, 900, 'bye'), 7.2, 3.4j, 10, (23, 45, 67), 'sql'}
x=set()
   
x
   
set()
x.add(100)
   
x
   
{100}
x.add()
   
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    x.add()
TypeError: set.add() takes exactly one argument (0 given)
x.add([1,2,3])
   
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    x.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
x.add(12,"Abc")
   
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    x.add(12,"Abc")
TypeError: set.add() takes exactly one argument (2 given)
x.add(True)
   
x
   
{True, 100}
x.add(100)
   
x
   
{True, 100}
x.add("THINK")
   

x
   
{True, 100, 'THINK'}



#update()-->var_name.update(iterable)
   
#wont accpet single value data type only collection data type accept
   
v=set()
   
v
   
set()
v.update(1)
   
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    v.update(1)
TypeError: 'int' object is not iterable
v.update(9.7)
   
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    v.update(9.7)
TypeError: 'float' object is not iterable
v.update(True)
   
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    v.update(True)
TypeError: 'bool' object is not iterable
v.update(3+4j)
   
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    v.update(3+4j)
TypeError: 'complex' object is not iterable
v.update("abc"
         v
         
SyntaxError: '(' was never closed
v.update("abc")
         
v
         
{'a', 'b', 'c'}
v.update([10,20,30])
         
v
         
{'c', 10, 'a', 20, 'b', 30}
v.update([[1,2,3,4]])
         
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    v.update([[1,2,3,4]])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
v.update([1,2,5,[34,67,98]])
         
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    v.update([1,2,5,[34,67,98]])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
v
         
{'c', 1, 2, 5, 10, 'a', 20, 'b', 30}
v.update(("a","b","c"))
         
v
         
{'c', 1, 2, 5, 10, 'a', 20, 'b', 30}
v.update({12:34,800:900,1000:2000})
         
v
         
{800, 'c', 1, 2, 5, 1000, 10, 12, 'a', 20, 'b', 30}
v.update({333,444})
         
v
         
{800, 'c', 1, 2, 5, 1000, 10, 12, 333, 'a', 20, 'b', 444, 30}
v.update("Hello")
         
v
         
{800, 'c', 1, 2, 'H', 5, 'o', 1000, 10, 12, 333, 'e', 'a', 'l', 20, 'b', 444, 30}
v.update(111,222,333,"xyz","python","java","enter",[4444,5555,9999])
         
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    v.update(111,222,333,"xyz","python","java","enter",[4444,5555,9999])
TypeError: 'int' object is not iterable
v.update("xyz","python","java","enter",[4444,5555,9999])
         
v
         
{1, 2, 5, 'o', 'p', 10, 'y', 12, 'e', 9999, 'z', 20, 'r', 30, 800, 'n', 'j', 5555, 't', 444, 'H', 333, 'l', 4444, 'c', 1000, 'x', 'a', 'h', 'b', 'v'}
w=set()
         
w
         
set()
w.update({500:900})
         
w
         
{500}
w.update([700,800])
         
w
         
{800, 700, 500}
w.update("abc")
         
w
         
{800, 'c', 'a', 500, 'b', 700}
w.update(["abc")
         
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
w.update(["abc"])
         
w
         
{800, 'c', 'a', 'abc', 500, 'b', 700}
w.update("abc",[12,45,67],(7,9,0),{56,89},{34:56,90:3})
         
w
         
{800, 'c', 0, 67, 34, 7, 9, 12, 45, 'a', 'abc', 500, 'b', 56, 89, 90, 700}
x=10,
         
x
         
(10,)
e=set()
         
e
         
set()
e.add(8)
         
e
         
{8}
#remove()--->discard()
         
#remove --->var_name.remove(element)
         
#discard--->var_name.discard(element)
         
w
         
{800, 'c', 0, 67, 34, 7, 9, 12, 45, 'a', 'abc', 500, 'b', 56, 89, 90, 700}
w.remove(800)
         
w
         
{'c', 0, 67, 34, 7, 9, 12, 45, 'a', 'abc', 500, 'b', 56, 89, 90, 700}
w.remove("python")
         
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    w.remove("python")
KeyError: 'python'
w.remove("abc")
         
w
         
{'c', 0, 67, 34, 7, 9, 12, 45, 'a', 500, 'b', 56, 89, 90, 700}
w.discard(700)
         
w
         
{'c', 0, 67, 34, 7, 9, 12, 45, 'a', 500, 'b', 56, 89, 90}
w.discard(999)
         
w
         
{'c', 0, 67, 34, 7, 9, 12, 45, 'a', 500, 'b', 56, 89, 90}
w.discard("python")
         

w
         
{'c', 0, 67, 34, 7, 9, 12, 45, 'a', 500, 'b', 56, 89, 90}
dir(list)
         
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
a=[1,2,3]
         
a
         
[1, 2, 3]
a.remove(6)
         
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    a.remove(6)
ValueError: list.remove(x): x not in list
#pop
         
#--->var_name.pop()
         
w.pop()
         
'c'
w.pop()
         
0
w.pop()
         
67


e={"snap","walmart","pen","box","chat"}
         
e.pop()
         
'box'
e.pop()
         
'chat'
e.pop()
         
'snap'
e
         
{'walmart', 'pen'}
e.pop
         
<built-in method pop of set object at 0x000001E2007DB760>
e.pop()
         
'walmart'
e.pop()
         
'pen'
e.pop()
         
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    e.pop()
KeyError: 'pop from an empty set'
w.clear()
         
w
         
set()
del w
         
w
         
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    w
NameError: name 'w' is not defined
del w
         
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    del w
NameError: name 'w' is not defined


#copy--->new_var_name=old_var_name
         
a={1,2,3,4}
         
b=a
...          
>>> d
...          
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> b
...          
{1, 2, 3, 4}
>>> a
...          
{1, 2, 3, 4}
>>> id(a)
...          
2070182476512
>>> id(b)
...          
2070182476512
>>> a.add(900)
...          
>>> a
...          
{1, 2, 3, 4, 900}
>>> b
...          
{1, 2, 3, 4, 900}
>>> b.update("evening")
...          
>>> b
...          
{1, 2, 3, 4, 900, 'i', 'e', 'n', 'g', 'v'}
>>> a
...          
{1, 2, 3, 4, 900, 'i', 'e', 'n', 'g', 'v'}
