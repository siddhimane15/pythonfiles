Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#TYPE CASTING--->
#Single value data type object
#int()
#float()
#complex()
#bool()
a=50
float(a)
50.0
complex(a)
(50+0j)
bool(a)
True


b=15.8
float(b)
15.8
int(b)
15
complex(b)
(15.8+0j)
bool(b)
True


c=15+8j
bool(c)
True
int(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> 
>>> 
>>> d=True
>>> int(d)
1
>>> float(d)
1.0
>>> complex(d)
(1+0j)
>>> 
>>> e=false
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    e=false
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> e=False
>>> int(e)
0
>>> float(e)
0.0
>>> complex(e)
0j
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
