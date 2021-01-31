# def sum(*args, **kwargs):
# 	result = 0
# 	for number in args:
# 		result += number
# 	print(result)

# sum(23, 1, 2, 4, 1, 1, 1, 1, 5, 10, hello = True, df = False)


# create a blueprint.
# function becomes a method when it's inside the class. 
# the first arg of the method is always the product of its class.

class car():

	def __init__(self, **kwargs): # init method creates the class.
		self.wheels =4 
		self.doors =2
		self.windows =2 
		self.seats =2
		self.paintjob = kwargs.get("paintjob", "black")
		self.price = kwargs.get("price", "$100")

	def start(self):
		print("Started the car...")

	# customizing the builtin method in the class.
	def __str__(self):
		return f"the car is {self.price}."

	def convertible(self):
		return "convert"

# extending the classes.
class convertible(car):

	def __init__(self, **kwargs):
		super().__init__(**kwargs) # extending the previous init w/ super()
		self.time = kwargs.get("time", "10 sec")

	def top_off(self):
		return "top off"

	def __str__(self):
		return f"the car without the top."


porsche = convertible(paintjob = "white", price ="$900")
print(porsche.time)
porsche.seats
porsche.top_off()
print(porsche)

# create the product using the blueprint.
# with specific specs. 
porsche = car(paintjob = "green", price = "$500")

# now using the method I created for the new product. 
porsche.start()
print(porsche)

mini = car()
print(mini.paintjob, mini.price)
print(mini)

print(porsche.windows)
# print(porsche.paintjob)
# list everything inside the class. 
# print(dir(car)) 