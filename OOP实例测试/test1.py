class Book(object):
	"""docstring for Book"""
	def __init__(self,name,id):
		self.name=name
		self.id=id
		print '<<' ,self.name,'>> has been build.'
	def updateBook(self,newid):
		self.id=newid
		print 'update success!'

class PriceBook(Book):
	"""docstring for PriceBook"""
	def __init__(self,name,id,price):
		Book.__init__(self,name,id)
		self.price=price
	def updatePrice(self,new_price):
		self.price=new_price
		print '<<',self.name,'>> have a new price.'