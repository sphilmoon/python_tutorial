#!/usr/local/bin python

# seven numeric operations:
def sum(a, b):
	return a + b

def diff(a, b):
	return a - b 

def prod(a, b):
	return a * b 

def quot(a, b):
	return a / b

def floor(a, b):
	return a // b

def remain(a, b):
	return a % b

def power(a, b):
	return a ** b

# user inputting integers:
a = int(input('Please input your first integer (a): '))
b = int(input('Please input your second integer (b): '))
print()

# defining results:
sum_result = sum(a, b)
diff_result = diff(a, b)
prod_result = prod(a, b)
quot_result = quot(a, b)
floor_result = floor(a, b)
remain_result = remain(a, b)
power_result = power(a, b)

# printing outputs: 
print('sum: ', sum_result)
print('difference: ', diff_result)
print('production: ', prod_result)
print('quotient: ' , quot_result)
print('floor: ', floor_result)
print('remaining: ', remain_result)
print('power: ', power_result)