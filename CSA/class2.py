Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
a=4
b=5
print(a+b)
9
print(a-b)
-1
print(b-a)
1
print(a*b)
20
print(a/b)
0.8
20
20
//multiplicaltio
SyntaxError: invalid syntax
print(a//b)
0
print(a%b)
4
print("float datatype")
float datatype
result=int(5.999)
print(result)
5
print("area of circle")
area of circle
r=5
print(3.14*r**)
SyntaxError: invalid syntax
print(3.14**r)
305.2447761824001
a=3j
b=2
z1=b+a
print(z1)
(2+3j)
z1=2+3j
z2=4-2j
print(z1+z2)
(6+1j)
z=3+4j
real_part=z.real
img_part=z.img
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    img_part=z.img
AttributeError: 'complex' object has no attribute 'img'. Did you mean: 'imag'?
print(z1*z2)
(14+8j)
r=5
print(3.14*(r*r))
78.5
print(3+3==6 and 3+3=9)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
a=3+3=6
SyntaxError: cannot assign to expression
a=3
b=6
print(a and b)
6
is_student=true
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    is_student=true
NameError: name 'true' is not defined. Did you mean: 'True'?
is_student = True
has_passed = False
print(is_student and has_passed)
False
print(is_student or has_passed)
True
x=10
if(x>5):
    print("x is greater than 5)
          
SyntaxError: unterminated string literal (detected at line 2)
if(x>5):
          print("x is greater than 5")
        else:
            
SyntaxError: unindent does not match any outer indentation level
if(x>5):
    print("x is greater than 5")
else:
    print("x is less than 5")

x is greater than 5
a=3
b=5
result = a>b
print(result)
False
x=True
print(not x)
False
z1=3+5j
z2=2+1j
print(z1 and z2)
(2+1j)
z3=z1+z2
z4=z1-z2
if(z3>z4):
    print("sum is greater")
else:
    print("sub is less")

    
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    if(z3>z4):
TypeError: '>' not supported between instances of 'complex' and 'complex'
age=18
has
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    has
NameError: name 'has' is not defined. Did you mean: 'hash'?
has_liscence=True
if age>18 and has_liscence:
    print("you can drive")


age=19
has_liscence = True
>>> if age>18 and has_liscence:
...     print("you can drive")
... 
you can drive
>>> "hello, world!"
'hello, world!'
>>> len(hello, world!)
SyntaxError: invalid syntax
>>> len("hello,world!")
12
>>> len(1,2,3,4,5,)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    len(1,2,3,4,5,)
TypeError: len() takes exactly one argument (5 given)
>>> len("1,2,3,4,5,")
10
>>> text="python"
>>> print(text{0})
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(text[0])
p
>>> print(text[3])
h
>>> name=Alice
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    name=Alice
NameError: name 'Alice' is not defined. Did you mean: 'slice'?
>>> name="Alice"
>>> greeting="hello,"+ name +"!"
>>> print(greeting.upper[])
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> message = greeting + name
>>> print(message)
hello,Alice!Alice
>>> text="python"
>>> print(text.strip())
python
