Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Dictionary
>>> 
>>> #update()--
>>> 
>>> 
>>> #update()-->
>>> #syntax:
>>> #without using inbuilt function  --->var_name[key]=value
>>> #with using inbuilt function--->var_name.update{key:value}
>>> a={}
>>> a
{}
>>> 
>>> a[10]=100
>>> a
{10: 100}
>>> a["abc"]=90
>>> a
{10: 100, 'abc': 90}
>>> a["hiiii"]=5
>>> a
{10: 100, 'abc': 90, 'hiiii': 5}
>>> a[5]="hello"
>>> a
{10: 100, 'abc': 90, 'hiiii': 5, 5: 'hello'}
>>> a[12]=15
>>> a
{10: 100, 'abc': 90, 'hiiii': 5, 5: 'hello', 12: 15}
>>> 
>>> 
>>> a.update{15:08}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> a.update{15:8}
SyntaxError: invalid syntax
a.update({15:8})
a
{10: 100, 'abc': 90, 'hiiii': 5, 5: 'hello', 12: 15, 15: 8}
a.update({"SHY":"siddhi"})
a
{10: 100, 'abc': 90, 'hiiii': 5, 5: 'hello', 12: 15, 15: 8, 'SHY': 'siddhi'}
a.update({"adb":"fgh",12:13,87:9,98.5:90})
a
{10: 100, 'abc': 90, 'hiiii': 5, 5: 'hello', 12: 13, 15: 8, 'SHY': 'siddhi', 'adb': 'fgh', 87: 9, 98.5: 90}

y={}
y
{}
y["x"]=y
y
{'x': {...}}
y["x"]="y"
y
{'x': 'y'}
y[90]="siddhi"
y
{'x': 'y', 90: 'siddhi'}
y.update({1:2,3:4,5:6,"aditi":"Tk","Sanika":"TS",15:8})
y
{'x': 'y', 90: 'siddhi', 1: 2, 3: 4, 5: 6, 'aditi': 'Tk', 'Sanika': 'TS', 15: 8}
y[15]
8
#keys()-->var_name.keys()
y.keys()
dict_keys(['x', 90, 1, 3, 5, 'aditi', 'Sanika', 15])

#values()-->var_name.values()
y.values()
dict_values(['y', 'siddhi', 2, 4, 6, 'Tk', 'TS', 8])
#items()
#var_name,items()
y.items()
dict_items([('x', 'y'), (90, 'siddhi'), (1, 2), (3, 4), (5, 6), ('aditi', 'Tk'), ('Sanika', 'TS'), (15, 8)])
d=y.items()
d
dict_items([('x', 'y'), (90, 'siddhi'), (1, 2), (3, 4), (5, 6), ('aditi', 'Tk'), ('Sanika', 'TS'), (15, 8)])

#key and values syntax:var_name[key]

#get():
#var_name.get(key,default value)

#var_name.setdefault(key,default value)
#var_name.pop(key,default value)
#var_name.popitem()
a={1:2,4:5,90:89,'abc':'aa','RTO':'OTP',111:222}
a.popitem()
















