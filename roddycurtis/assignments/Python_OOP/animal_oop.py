class Animal(object):
	def__init__(self,name='pet',health=100):
		self.name=name
		self.health=health
	def walk(self):
		self.health-=1
	def run(self):
		self.health-=5
	def displayHealth():
		print self.name
		print self.health


animal=Animal('Animal')

animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
	def__init__(self):
		super(Dog, self).__init__()
		self.health=150

	def pet(self):
		self.health+=5


dog=Dog('Dog')

dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
	def__init__(self):
		super(Dragon,self).__init__()
		self.health+=70

	def fly(self):
		self.health-=10
	def displayHealth(self):
		super(Dragon,self).displayHealth()
		print 'This is A Dragon!'


dragon=Dragon('Dragon')

dragon.walk().walk().walk().fly().fly().displayHealth()
























