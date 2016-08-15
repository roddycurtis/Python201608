class Bike(object):
	def __init__(self,price=100,max_speed=25):
		self.price=price
		self.max_speed=max_speed
		self.miles=0
	
	def display_info(self):
		print 'Price:'+str(self.price)
		print 'Max Speed:'+str(self.max_speed)
		print 'Total Miles:'+str(self.miles)

	def riding(self):
		self.miles +=10
		print 'Riding'

	def reverse (self):
		self.miles -=10
		print 'Reverse'


bike1=Bike(100,10)
bike1.riding().riding().riding().reverse().display_info()

bike2=Bike(200,20)
bike2.riding()
bike2.riding()
bike2.riding()
bike2.reverse()
bike2.display_info()

bike3=Bike(300,30)
bike3.riding()
bike3.riding()
bike3.riding()
bike3.reverse()
bike3.display_info()