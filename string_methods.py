Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
'Evening'
'Evening'

b.removeprefix("gn")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    b.removeprefix("gn")
NameError: name 'b' is not defined

==================================================================================== RESTART: Shell ====================================================================================
b='Evening'
b.removeprefix("gn")
'Evening'

b.removeprefix ("ng)
                
SyntaxError: unterminated string literal (detected at line 1)
b.removeprefix ("ng")
                
'Evening'
b.removesuffix("g")
                
'Evenin'
b.removesuffix("gn")
                
'Evening'
b.removesuffix("ng")
                
'Eveni'
b.removesuffix("ning")
                
'Eve'

b.removeprefix("e")
...                 
'Evening'
>>> 'Evening'
...                 
'Evening'
>>> b.removeprefix("E")
...                 
'vening'
>>> 
=============================================================== RESTART: Shell ==============================================================
>>> r="PROGRAMMINGPRO"
...                 
>>> 
>>> 
>>> 
>>> 

... 
>>> r.index("P")
...                 
0
>>> 
>>> r.index("P",1)
...                 
11
>>> 
>>> r.index("P",1,10)
...                 
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    r.index("P",1,10)
ValueError: substring not found
>>> r.index("R")
...                 
1
>>> r.index("R",2)
...                 
4
>>> 
