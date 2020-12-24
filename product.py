import database
class product:
	def __init__(self , name , quantity , rate , discount , tax):
		self.name = name
		self.quantity = quantity
		self.rate = rate
		self.discount = discount
		self.tax = tax
		self.id = (self.name + str(self.quantity) + str(self.rate) + str(self.discount) + str(self.tax) + str(database.num))
		database.num += 1
	def setname(self , name):
		self.name = name
	def setquantity(self , quantity):
		self.quantity = quantity
	def setrate(self , rate):
		self.rate = rate
	def setdiscount(self , discount):
		self.discount = discount	
	def settax(self , tax):
		self.tax = tax
	def getname(self):
		return self.name
	def getquantity(self):
		return self.quantity
	def getrate(self):
		return self.rate
	def getdiscount(self):
		return self.discount
	def gettax(self):
		return self.tax
	def getid(self):
		return self.id
	def addquantity(self , next):
		self.quantity = self.quantity + next
	def productselling(self , quantity):
		self.quantity = self.quantity - quantity
		taxcost = quantity*((self.rate * self.tax)/100)
		discountcost = quantity*((self.rate * self.discount)/100)
		itemcost = quantity*(self.rate)
		final = [itemcost , discountcost , taxcost]
		return final
