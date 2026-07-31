Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#operator-->operator are symbol

#operators are symbol we are using to perform certain operations
#arithmetic operators--->
# +
a=10
b=20
a+b
30
2.3+5.6
7.8999999999999995
1+2j + 3+4j
(4+6j)
True+False
1
# + support for--->int,float,complex,string,tuple,set,bool

#not support for--->set,dict
# -
10-5
5
3.4-1.2
2.2
True-True
0
2+2j-4+5j
(-2+7j)
"Hii"-"abc"
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    "Hii"-"abc"
TypeError: unsupported operand type(s) for -: 'str' and 'str'
l=[1,2,4]
k=[5,9,6]
l-k
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    l-k
TypeError: unsupported operand type(s) for -: 'list' and 'list'
w=(11,12)
w1=(56,78)
w-w1
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    w-w1
TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'
u={1,2,3,4}
u1={7,8,9,3}
u-u1
{1, 2, 4}
u={1,2,3}
u1={2,3,4,5}
u-u1
{1}
u
{1, 2, 3}
u1
{2, 3, 4, 5}
u.difference(u1)
{1}
u1.difference(u)
{4, 5}
#- support for -->int,float,complex,bool,set
#not support for ----> str,list,tuple,dict

a*b
200
2.1*2.4
5.04
True*True
1
"HIIII"*"HELLO"
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    "HIIII"*"HELLO"
TypeError: can't multiply sequence by non-int of type 'str'
"Hii"*2
'HiiHii'
k={1,2,3}
k*3
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    k*3
TypeError: unsupported operand type(s) for *: 'set' and 'int'
#* support for -->int,float,complex,bool,str,list,tuple

#/--->division operator
#(True Division operator)--->it only support for single value data type
#o/p==Decimal format
10/5
2.0
2.3/5
0.45999999999999996
True/False
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    True/False
ZeroDivisionError: division by zero
1/0
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
0/1
0.0
a=(2+4j)/2
a
(1+2j)
(4+5j)/2+5j
(2+7.5j)
"hello"/2
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    "hello"/2
TypeError: unsupported operand type(s) for /: 'str' and 'int'
[1,2,3]/2
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    [1,2,3]/2
TypeError: unsupported operand type(s) for /: 'list' and 'int'
(1,2,3)/2
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    (1,2,3)/2
TypeError: unsupported operand type(s) for /: 'tuple' and 'int'
#//--->floor division --->always o/p quotient
s=1234
t=7
s/t
176.28571428571428
s//t
176
a=1234
a//100
12
a//10
123
a//1000
1

#%--->if we want to print remainder then you use %
10%2
0
15%2
1
121%10
1


#**-->power
a=10
a**3
1000
a*3
30
#divmod()--->always accept 2 para-->divmod(x,y)
s=10
a=3
s/a
3.3333333333333335
s//a
3
s%a
1
divmod(s,a)
(3, 1)
#Bitwise operator
#6 type--->1.Bitwise AND OPERATOR(&) 2.Bitwise OR OPERATOR(|) 3.Bitwise NOR OPERATOR(^)  4.Bitwise NOT OPERATOR(~ til negation) 5.Bitwise left shift operator  6.Bitwise right shift operator
bin(10)
'0b1010'
bin(20)
'0b10100'
bin(90)
'0b1011010'
bin(15)
'0b1111'
bin(8)
'0b1000'
'0b10100'
'0b10100'
#bitwise AND Operator
a=10
b=2
a&b
2
x=45
y=70
45&70
4
x&y
4
bin(45)
'0b101101'
bin(70)
'0b1000110'
bin(98)
'0b1100010'
bin(85)
'0b1010101'
98&85
64
bin(64)
'0b1000000'





























































































































































































































... 
... 
>>> 
>>> x=77
>>> y=69
>>> x|y
77
>>> bin(77)
'0b1001101'
>>> bin(69)
'0b1000101'
>>> a=120
>>> b=99
>>> bin(120)
'0b1111000'
>>> bin(99)
'0b1100011'
>>> 120|99
123
>>> bin(123)
'0b1111011'
>>> x=39
>>> y=7
>>> 39&7
7
>>> bin(39)
'0b100111'
>>> bin(7)
'0b111'
>>> 39|9
47
>>> bin(47)
'0b101111'
>>> 39^9
46
>>> bin(46)
'0b101110'
39|7
39
39^7
32
bin(39)
'0b100111'
bin(32)
'0b100000'
