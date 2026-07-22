Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
z=["welcome","dowork-fast","next-level","top-data","clock","volume","super-menu"]
#weldone,dowork-fast next-level
#lebel

#level
#pot
#ock
#kco
#ume
#menu
#unem
#ata
#lov

z=["weldone","dowork-fast","next-level","top-data","clock","volume","super-menu"]
z.append[0:3:1]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    z.append[0:3:1]
TypeError: 'builtin_function_or_method' object is not subscriptable
z[0:3:1]
['weldone', 'dowork-fast', 'next-level']
z[2][5:10:1]
'level'
>>> z[3][-6:-9:-1]
'pot'
>>> z[4][2:5:1]
'ock'
>>> z[4][-1:-4:-1]
'kco'
>>> z[5][3:6:1]
'ume'
>>> z[6][6:10:1]
'menu'
>>> z[6][-1:-4:-1]
'une'
>>> z[6][-1:-5:-1]
'unem'
>>> z[3][5:8:1]
'ata'
>>> z[5][-4:-7:1]
''
>>> z[5][-4:-7:-1]
'lov'
>>> dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dir(string)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    dir(string)
NameError: name 'string' is not defined. Did you forget to import 'string'?
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
