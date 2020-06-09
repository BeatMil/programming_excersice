class Car:
	def __init__(self, name):
		self.name = name
		self.speed = 0

	def __str__(self):
		return "%s\n%s"%(self.name,self.speed)

	def speed_up(self, speed):
		self.speed += speed



car01 = Car("Beat")
car02 = Car("Ming")

print(car01)
car02.speed_up(100)
print(car02)



# car = Car("Beat")
# print(car) 
# print(car.name)
# print(car.speed)
# car.speed_up(100)
# print(car.speed)
