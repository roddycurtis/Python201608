class Car(object):     
	def__init__(self,price=10000,speed=40,fuel=full,mpg=20):
		self.price=price
		self.speed=speed
		self.fuel=fuel
		self.mpg=mpg
		if self.price>10000:
			self.tax=.15
		else:
			self.tax=.12

		self.display_all()


	def display_all(self):
		print 'Price: '+str(self.price)
		print 'Speed: '+str(self.speed)
		print 'Fuel: '+str(self.fuel)
		print 'MPG: '+str(self.mpg)

car1=car(2500,20,full,25)
car2=car(2500,20,full,25)
car3=car(2500,20,full,25)
car4=car(2500,20,full,25)
car5=car(2500,20,full,25)
car6=car(2500,20,full,25)

