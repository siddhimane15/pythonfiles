Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Assignment operator
a=100
a+=100
a
200
a+=300
a
500
a-=250
a
250

x=100
x+=50
x
150
x-=50
x
100

x*=2
x
200
x/=2
x
100.0
x%=2
x
0.0

y=123
y//3
41

a=8
a**=3
a
512

#membership operator
#in,not in
a=[10,20,40,"abc","xyz"]
40 in a
True
100 in a
False
"abc" in a
True
"ABC" in a
False
40 not in a
False
100 not in a
True

k="Good luck"
"k" in k
True
"*" in k
False
"g" in k
False
"G" in k
True
"k " not in k
True
"k" not in k
False


#identity operator
# is , is not
a=[10,20,40,"abc","xyz"]
40 is a
False
a=[10,20,40,"abc","xyz"]
b=[10,20,40,"abc","xyz"]
a is b
False
a is not b
True
b is a
False

a=100
b=200
c=300
id(a)
140731543048408
id(b)
140731543051608
id(c)
1732756149840
a is b
False


a=100
b=200
c=100
id(a)
140731543048408
id(b)
140731543051608
id(c)
140731543048408
a is b
False
a is c
True
a is not b
True
a is not b
True
a is not c
False

#Relational operator
# <,<=>,>=,==,!=
#Logical opeartor
# And,Or,Not
a=10
b=5
a>5
True
a>=5
True
b>3
True
a>5 and b>3
True
a<100 and b<150
True
10<100
True
5<50
True

a=10
b=5
a>5 or b>3
True
0/1
0.0
1/0
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
a=100
not a
False

b=True
not b
False

c="Hello"
not c
False
k=false
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    k=false
NameError: name 'false' is not defined. Did you mean: 'False'?
k=False
not k
True
not 0
True
not 1
False
d={1,2,3,4}
not d
False

not{1,2,3}
False
12>5
True
"one">"two"
False
ord("o")
111
ord("n")
110
ord("e")
101
3>3
False
3>=3
True

45>=50
False
45>=45
True
45>=35
True
5000<=600
False

500==500
True
(0.1)+(0.2)==0.3
False
0.1+0.2
0.30000000000000004
0.3==0.3
True

bin(15)
'0b1111'
#bitwise operator
#bitwise left shift operator(>>) & bitwise left shift operator(<<)
#bitwise right shift operator(<<)
170&80
0
170|80
250
170^80
250
bin(170)
'0b10101010'
128+64+32+16+8+4+2+1
255
bin(250)
'0b11111010'
>>> bin(56)
'0b111000'
>>> 32+16+8
56
>>> 32+16
48
>>> 48+8
56
>>> 56>>2
14
>>> bin(14)
'0b1110'
>>> 47>>2
11
>>> bin(11)
'0b1011'
>>> bin(47)
'0b101111'
>>> 47<<2
188
>>> bin(188)
'0b10111100'
>>> 4+8+16+32+64
124
>>> 4+8+32+16+128
188
>>> #bitwise not operator
>>> #~
>>> #syntax: n=-(n+1)
>>> a=10
>>> ~a
-11
>>> -(10+1)
-11
