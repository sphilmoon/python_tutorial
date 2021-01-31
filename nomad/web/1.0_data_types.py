#!/usr/local/bin python

### Data types

a_string = "as it is"
a_number = 3
a_float = 3.14
a_boolean = False
a_none = None

### Lists (mutable)

days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
print(days)
days.append("Sat")
days.insert(0, "Sun")
print(days)
days.extend(("the", "calendar", "week"))
print(days)
print(type(days))

### Tuples (immutable)

coffee = ("Starbucks", "Teavana", "original")
print(type(coffee))

### Dictionary (mutable)

goldfinger = {
	"name": "Goldfinger",
	"age": "unknown",
	"height": 188,
	"nationality": "Germany",
	"sniper": True,
	"allergies": ["yankee candle", "coffee"]
}

print(goldfinger)
goldfinger["lethal"] = True
print(goldfinger)

### Built-in functions

number = "22"
print(number)
print(type(number))

integer = int(number)
print(integer)
print(type(integer))

	# creating my own functions using 'def'

def say_whatsup(who=""): # '=' sign don't require an input.
	print("what's up,", who)

say_whatsup()
say_whatsup("Goldfinger!")

	# I can also add a default value if any arg don't exist.
def p_subtraction(a, b=0): 
	print(a - b)

p_subtraction(2, 20) # print output.

### Returns. 
	# Use return to output the result/value inside the function. 

def r_subtraction(a, b=0): 
	return(a - b)

r_subtraction(2, 20) # no output.
	# comparison print vs return
p_result = p_subtraction(2, 20) # none bc can't input in the function. 
r_result = r_subtraction(2, 20) # returns the value. 
print(p_result, r_result)

### Positional argument 
# position doesn't matter when you assign values. 

def summation(a, b):
	return a + b

sum_result = summation(b=-4, a=3)
print(sum_result)

def say_hello(name, age):
	return f"hello {name}, you are {age} old."

hello = say_hello(name="phil", age=22)
print(hello)
#print(say_hello("phil", 22))

### IF_ELSE

def sum(a, b):
	if type(a) and type(b) is str:
		return None
	else:
		return a + b

print(sum(22, "2"))

def check_id(age):
	if age < 21:
		print(f"you're {age}. Minors cannot enter bars.")
	elif age == 21:
		print("Young blood!! Welcome!")
	elif 21 < age < 25:
		print("You're a rookie! Welcome!")
	else:
		print("Go ahead. Enjoy the drink.")
	
check_id(22)

### For loops

days = ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]

for day in days:
	if day is "Wed":
		break 
	else:
		print(day)

for letter in "goldfinger": # can also works with strings. 
	print(letter)

### Modules

from math import ceil, fsum

# printing the smallest integer of the float x. 
print(ceil(3.14))
