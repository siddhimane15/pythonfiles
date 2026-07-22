Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s="python"
"programming".join(s)
'pprogrammingyprogrammingtprogramminghprogrammingoprogrammingn'


=============================================================== RESTART: Shell ==============================================================
s="python"
"_".join(s)
'p_y_t_h_o_n'
".".join(s)
'p.y.t.h.o.n'
"-".join(s)
'p-y-t-h-o-n'

 
A="SIDDHI"
"123".join(A)
'S123I123D123D123H123I'
B="smart"
"@".join(B)
's@m@a@r@t'


a="morning"
a.split("n")
['mor', 'i', 'g']
B="Youger"
B.split("r")
['Youge', '']
C="Pyhton is very easy language"
C.spilt("is")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    C.spilt("is")
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
C="Pyhton is very easy language"
C.split("is")
['Pyhton ', ' very easy language']


a="morning"
a.rsplit("n")
SyntaxError: multiple statements found while compiling a single statement
a="morning"
a.split("n")
['mor', 'i', 'g']
s="Occupado"
s.rsplit("p")
['Occu', 'ado']
H="Harsh"
H.split("s")
['Har', 'h']


a="morning"
a.lsplit("n")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.lsplit("n")
AttributeError: 'str' object has no attribute 'lsplit'. Did you mean: 'rsplit'?
a="morning"


a="Siddhi"
a.strip("S")
'iddhi'
B="PYTHON"
B.strip("H")
'PYTHON'
C="GOOD LUCK"
C.strip("D")
'GOOD LUCK'


a=" Programming "
a.strip("g")
' Programming '

b="  Programming"
b.strip()
'Programming'


c="  Programming "
c.rstrip("  ")
'  Programming'
d="@#$%Siddhi"
d.rstrip("@#$")
'@#$%Siddhi'
c="@##$%yellow"
c.rstrip("w")
'@##$%yello'


c="  Programming "
c.lstrip("  ")
'Programming '

d="@#$%Siddhi"
d.lstrip("@#$")
SyntaxError: multiple statements found while compiling a single statement
d="@#$%Siddhi"
d.lstrip("@#$")
'%Siddhi'
c="@##$%yellow"
c.lsytrip("@")
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    c.lsytrip("@")
AttributeError: 'str' object has no attribute 'lsytrip'. Did you mean: 'lstrip'?
c="@##$%yellow"
c.lstrip("@")
'##$%yellow'



a="siddhi"
a.upper()
'SIDDHI'
b="harsh"
b.upper()
'HARSH'
c="aditi"
c.upper()
'ADITI'


a="MARCH"
a.lower()
'march'
C="YARAA"
C.lower()
'yaraa'
D="DOG"
D.lower()
'dog'


a="siddhi"
a.swapcase()
'SIDDHI'
b="SIDDHI"
b.swapcase()
'siddhi'
C="sidHYFCBNKJHiin"
C.swapcase()
'SIDhyfcbnkjhIIN'


S="yinbbncfcvnm"
S.capitalize()
'Yinbbncfcvnm'
v="jhncx bhzjjknz nxvcbjknvxcm "
v.capitalize()
'Jhncx bhzjjknz nxvcbjknvxcm '
r="uhjnszuhnmcv"
r.capitalize()
'Uhjnszuhnmcv'


s="hjdnvznb jhnm"
s.title()
'Hjdnvznb Jhnm'
v="nkmnxvcm cnlk xmv "
v.title()
'Nkmnxvcm Cnlk Xmv '
h="jjn k  kmm mnkml "
h.title()
'Jjn K  Kmm Mnkml '



a="hjnxcv "
a.isaplha()
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    a.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
a="mhnnnnn"
a.isalpha()
True
b="yijnmb123"
b.isalpha()
False
g="uhbnvx"
g.isaplha()
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    g.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
g.isalpha()
True


a="123gg"
a.isalnum()
True
c='hhnmvcxnm1244"
SyntaxError: unterminated string literal (detected at line 1)
c="nm mcxvmn6776"
c.isalnum()
False
d="ytgvhbjxcv567"
d.isalnum()
True


a="1232456"
a.isdigit()
True
p="8097787"
p.isdigit()
True
y="6798nnmnn"
y.isdigit()
False


c=""
c.isspace()
False

g="  "
g.isspace()
True
h="     "
h.issspace()
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    h.issspace()
AttributeError: 'str' object has no attribute 'issspace'. Did you mean: 'isspace'?

h.isspace()
True


a="innjmm"
a.isupper()
False
b="IHB"
b.isupper()
True
c="JNBhhhh"
c.isupper()
False


a="jbvccvHHJJ"
a.islower()
False
o="mnm"
o.islower()
True
o="HGBNM"
o.islower()
False


a="Siddhi"
a.istitle()
True
a="gbnbmnb hujknnk"
a.istitle()
False
a="gvbvbhn uihkbnm sdfffffffff"
a.islower()
True

a="kjnhjnm"
a.startswith("k")
True
b="uhbnmeafdszcvxjm "
b.startswith("l")
False
c="piuugb mfsdvcx"
>>> c.startswith("p")
True
>>> 
>>> 
>>> a="kjnhjnm"
... a.endswith("k")
SyntaxError: multiple statements found while compiling a single statement
>>> a.endswith("m")
True
>>> b="jjnm"endswith(
...     
SyntaxError: '(' was never closed
>>> b="uhbnmeafdszcvxjm "
>>> b.endswith("m")
False
>>> c="uhbfzdsjcvnx m
SyntaxError: unterminated string literal (detected at line 1)
>>> c="gvgghbnsnjdhunjmdf"
>>> c.endswith("g")
False
>>> 
>>> import keyword
>>> keyword.is("if")
SyntaxError: invalid syntax
>>> import keyword
\
>>> import keyword
>>> keyword.iskeyword("if")
True
>>> 
...   
>>> 
>>> a.isidentifier("Siddhi)
...                
SyntaxError: unterminated string literal (detected at line 1)
>>> s="siddh"
...                
>>> s="siddhi"
...                
