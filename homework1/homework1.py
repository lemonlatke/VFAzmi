#File: homework1.py

# --- Variables and Data Types --- 

a = 10
print(a)
print(type(a)) 
# a is an integer, a regular counting number

b = 1.5
print(b)
print(type(b))
# b is a float, a decimal value

c = 3j
print(c)
print(type(c))
# c is a complex number, a number with a real and an imaginary part

d = "hello"
print(d)
print(type(d))
# d is a string, a line of characters

e = [1, 2, 3]
print(e)
print(type(e))
# e is a list, multiple elements stored together

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f))
# f is a dictionary, keys and values paired together 

g = (1,2)
print(g)
print(type(g))
# g is a tuple, values in a single variable whose orders cannot be changed

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h))
# h is a list, multiple elements stored together

i = True
print(i)
print(type(i))
# i is a boolean, storing true or false values

j = None
print(j)
print(type(j))
# j is a NoneType, equivalent to null, value holds nothing

k = [True, "blue", 12]
print(k)
print(type(k))
# k is a list, multiple elements stored together

l = str(14)
print(l)
print(type(l))
# l is a string, a line of characters

m = 1e4
print(m)
print(type(m))
# m is a float, a decimal value

"""
# 
1) I found a total of nine datatypes
2) integer, float, complex, string, list, dictionary, tuple, boolean, NoneType
3) d, l: strings ; e, k, h: lists ; b, m: floats
4) l was a string. It was not an integer because the variable is predefined to be read as a row of characters in lieu of digits.
5) binary variable, code written below

"""

n = 0b101010
print(n) # The meaning of life
print(type(n)) 
# n is a binary, a number expressed in ones and zeroes

# --- Booleans ---

print(10 > 9)
# true, 10 is greater than 9
print(10 == 9)
# false, 10 is not equal to 9
print(10 <= 9)
# false, 10 is not less than or equal to 9
print(bool("abc"))
# true, the string has some value
print(bool(123))
# true, a non-zero integer is true
print(bool(["apple", "cherry", "banana"]))
# true, list has values
print(bool(True))
# true, literally true
print(bool(False))
# false, literally false
print(bool(0))
# false, 0 is false
print(bool(""))
# false, string is empty
print(bool(" "))
# true, string has some value
print(bool())
# false, empty tuple
print(bool([]))
# false, empty list
print(bool({}))
# false, empty dictionary
print(bool(True and False))
# false, true and false cannot be, so false
print(bool(True and True))
# true, both values are true, so true
print(bool(False and False))
# false, both values are false, so false
print(bool(True or False))
# true, only one needs to be true, and is, so true
print(bool(True or True))
# true, both values true, so true
print(bool(False or False))
# false, both values false, so false
print(bool(not(False)))
# true, negates false, so true
print(bool(not(True)))
# false, negates true, so false

"""
#
1) If the word 'and' was present alongside false, the program always returned false.
2) I was not surprised by any answer
3) print(bool(str(14))); the string has some value and so will return true
4) print(bool(not(not(False)))); negates a negated false, so returns false

"""

# --- Operators ---
# -Arithmetic-

print(10 + 5)
# 15, performs addition
print(10 - 5)
# 5, performs subtraction
print(2 * 4)
# 8, performs multiplication
print(6 / 3)
# 2, performs division
print(5 % 2)
# 1, shows remainder after division
print(3 ** 2)
# 9, performs exponentiation
print(15 // 2)
# 7, performs division and rounds down

# -Comparison-

print(5 == 2)
# false, calls boolean 
print(10 != 10)
# false, calls boolean
print(2 < 5)
# true, calls boolean
print(12 > 5)
# true, calls boolean
print(5 <= 6)
# true, calls boolean
print(1 >= 10)
# false, calls boolean

# -Assignments-

x = 5
x += 5
print(x)
# 10, adds to stored value, stores new value
x -= 4
print(x)
# 6, subtracts from stored value, stores, new value
x *= 3
print(x)
# 18, multiplies stored value, stores new value

"""
#
1) 'and' returns true iff all expressions are true. (True and True returns True, True and False returns False)
2) 'or' returns true if any expression true. (False or True returns True, False or False returns False)
3) 'not' negates the expression that follows. (not(False) returns True, not(True) returns False)

1) '/' is division that will return the exact value as a float, "//" is floor division that will return the smallest near integer.
2) '%' is modulus, will return the remainder of the quotient, '//' returns the quotient without the remainder
3) I would use '%'. (ex. 25 % 2 = 1)
4) Assignment operators perform an operation on the called variable, then store a new value into the variable.

"""

# ---Strings---

my_string = "hello"
print(my_string)
# prints: hello
print(my_string[0])
# prints: h
print(my_string[1])
# prints: e
print(my_string[2])
# prints: l
print(my_string[3])
# prints: l
print(my_string[4])
# prints: o
print(my_string[-1])
# prints: o
print(my_string[1:3])
# prints: el
print(my_string[0:5:2])
# prints: hlo
print(len(my_string))
# prints: 5
print(my_string + " goodbye")
# prints: hello goodbye
print(7 * my_string)
# prints: hellohellohellohellohellohellohello

"""
# 
1) Slicing involves separating pieces of the stored string.
2) Prints: Hello, my name is Oski.
3) Prints: Hello, my name is Oski.
4) The second command is a more concise way to write the first command.

"""

name = "Oski"
print("Hello, my name is", name)
print(f"Hello, my name is {name}")

# ---Terminal Commands---
"""
#
1) cd: change directories
    cd python_decal_fa25
2) ls: lists contents of current directory
    ls
3) ls -a: lists hidden files
    ls -a
4) mkdir: makes directory
    mkdir homework1
5) cat: concatnates script, displays code without running
    cat datatypes.py
6) pwd: prints working directory
    displays address of current directory
7) cd ..: changes directory to parent directory
    cd ..
8) cd .: remains in current directory
    cd .
9) cd ~: changes directory to root directory
    cd ~
10) cp: copies file to a directory
    cp homework1.py /c/Users/pseud/python_decal_fa25/VFAzmi
11) mv: moves file to a directory, or renames file
    mv homework1.py /c/Users/pseud/python_decal_fa25/VFAzmi
12) rm: removes file
    rm homework1.py
13) clear: clears terminal of all previous lines
    clear
14) grep: searches for keyword or pattern in file, prints line that includes search term
    grep "Hello, World!" datatypes.py
    
"""
"""
#
1)  a) touch: creates file
        touch homework1.py
    b) git commit -m: records commit with a message
        git commit -m "First light"
    c) git status: displays status of repository
        git status
2) ls displays all the files and children directory within the current directory, while ls -a displays the aforementioned including hidden files.
3) a hidden file that isn't usually displayed, in .git case it holds information for our version control
4)  a) -m : message flag for git commit
        git commit -m <message>
    b) -A : flag for git add that stages all changes in the current directory
        git add -A
    c) -l : flag for ls that lists contents in a long listing format
        ls -l

"""