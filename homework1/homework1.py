# File: homework1.py
# --- Variables and Data Types ---
a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals
b = 1.5
print(b)
print(type(b)) # b is a float, a number with a decimal
c = 3j
print(c)
print(type(c)) # c is a complex number, a number with a real and imaginary part
d = "hello"
print(d)
print(type(d)) # d is a string, a sequence of characters
e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, a collection of items
f = {"name": "Ella", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, a collection of key-value pairs
g = (1, 2)
print(g)
print(type(g)) # g is a tuple, an ordered collection of items that cannot be changed
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, a collection of items
i = True
print(i)
print(type(i)) # i is a boolean, a value that can be either True or False
j = None
print(j)
print(type(j)) # j is a NoneType, a special type that represents the absence of a value
k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, a collection of items
l = str(14)
print(l)
print(type(l)) # l is a string, a sequence of characters
m = 1e4 
print(m)
print(type(m)) # m is a float, a number with a decimal
# 1. 9 different data types
# 2. int, float, complex, str, list, dict, tuple, bool, NoneType
# 3. variables l, d are strings; k, h, e are lists; m, b are floats
# 4. l is a string, not an integer because the str() function converts the integer 14 into a string representation of the number
'''
n = range(6)
print(n)
print(type(n)) # n is a range, a sequence of number
'''
print(10 > 9) # True, because 10 is greater than 9)
print(10 == 9) # False, because 10 is not equal to 9
print(10 <= 9) # False, because 10 is not less than or equal to 9
bool("abc") # True, because the string is not empty
bool(123) # True, because the number is not zero
bool(["apple", "cherry", "banana"]) # True, because the list is not empty
bool(True) # True, because the value is True
bool(False) # False, because the value is False
bool(0) # False, because the number is zero
bool(" ") # False, because the string is empty
bool("  ") # True, because the string is not empty (it contains whitespace)
bool([]) # False, because the list is empty
bool({}) # False, because the dictionary is empty
bool(True and False) # False, because one of the values is False
bool(True and True) # True, because both values are True
bool(False and False) # False, because both values are False
bool(True or False) # True, because one of the values is True
bool(True or True) # True, because both values are True
bool(False or False) # False, because both values are False
bool(not(False)) # True, because the value is False and not(False) is True
bool(not(True)) # False, because the value is True and not(True) is False
'''
Bool recognizes it as true because one option is true (only with the "or")
I was surprised that whitespace counts as an input for a string
'''
bool("9") # True, because the string is not empty
bool(0) # False, because the number is zero
print(10+5) # 15, + performs addition
print(10-5) # 5, - performs subtraction
print(2 * 4) # 8, * performs multiplication
print( 6/3) # 2.0, / performs division
print(2**3) # 8, ** performs exponentiation
print(15//2) # 7, // performs floor division
print(5==2) # False, == checks if two values are equal
print(10 !=10) # True, != checks if two values are not equal
print(2<5) # True, < checks if the left value is less than the right value
print(12>5) # True, > checks if the left value is greater than the right value
print(5<=6) # True, <= checks if the left value is less than or equal to the right value
print(1 >=10) # False, >= checks if the left value is greater than or equal to the right value
x = 5
x += 5
print(x) # 10, += adds the right value to the left value and assigns the result to the left value
x -= 4
print(x) # 6, -= subtracts the right value from the left value and assigns the result to the left value
x *= 3
print(x) # 18, *= multiplies the left value by the right value and assigns the result to the left value
# and combines two boolean expressions and returns True if both are True, otherwise it returns False
bool(True and 9) # True, because both values are True
bool(True and 0) # False, because one value is false
# or combines two boolean expressions and returns True if at least one is True
bool(True or 0) # True, because one value is True
bool(False or 0) # False, because both values are False
# not negates a boolean expression and returns True if the expression is False, otherwise it returns False
bool(not(0)) # True, because the expression is False
bool(not(1)) # False, because the expression is True
'''
/ performs division and yields a float, while // performs floor division and yields an integer
% performs modulus and returns the remainder of a division operation, while // returns the quotient of a division operation rounded down to the nearest integer
use % to calculate the remainder
assigns a value to a variable using the = operator and demonstrates different arithmetic operations
'''
my_string = "hello"
print(my_string) # hello, prints the value of the variable my_string
print(my_string[0]) # h, prints the first character of the string
print(my_string[1]) # e, prints the second character of the string
print(my_string[2]) # l, prints the third character of the string
print(my_string[3]) # l, prints the fourth character of the string
print(my_string[4]) # o, prints the fifth character of the string
print(my_string[-1]) # o, prints the last character of the string
print(my_string[1:3]) # el, prints the second and third characters of the string
print(my_string[0:5:2]) # hlo, prints every second character of the string
len(my_string) # 5, returns the length of the string
print(my_string + "goodbye") # hellogoodbye, concatenates the two strings
print(my_string * 7) # hellohellohellohellohellohellohello, repeats the string 7 times
# slicing allows you to extract a portion of a string by specifying the starting and ending indices, as well as an optional step value
# i sliced in the string to get the first 3 characters, then sliced again to get the last 2 characters, and finally sliced again to get every second character
name = "Oski"
print("Hello, my name is", name)
name = "Oski"
print(f"Hello, my name is {name}")
# the f string allowed me to embed the name because of the specified variable instead of typing out the phrase
'''
cd
changes directories
example: cd documents
ls
lists files in directory
example: ls
ls -a
lists all files, including hidden
example: ls -a
mkdir
makes directory
example: mkdir python_spring27
cat
discplays contents of a file
example: cat homework1.py
pwd
print working directory
example: pwd
cd ..
changes directories to parent directory
example: cd ..
cd . 
changes directory to current directory
example: cd .
cd ~
changes directory to home directory
example: cd ~
cp
copy file
example: cp homework1.py homework1_copy.py
mv
moves file
example: mv homework1.py homework1_copy.py
rm
remove file
example: rm homework1_copy.py
clear
clears terminal
example: clear
grep
searches for a string in file
example: grep "Oski" homework1.py
round
rounds a number to nearest integer
example: round(26.7)
elif
elif is used to check for multiple conditions in an if statement
example: elif score >= 80:
    print("You got a B")
enumerate
enumerate is used to loop through a list and get the index and value of each item
example:enumerate(my_list)
ls lists all files in a directory but ls -a lists all files including hidden files
hidden files are files that are not normally visible in a directory (usually start with a .)
-c runs a single command
-x ignores the first line of the script and runs the rest
-O runs the script with specified options
'''