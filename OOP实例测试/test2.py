"""just to be more more ....emmmm"""
"""emmmmmmm,all right"""
user_num=0
class basic(object):
	"""docstring for basic"""
	def __init__(self,name,create_date):
		self.name=name
		self.date=create_date
		print 'You creat',self.name,'in ',self.date
	def update_name(self,new_name):
		old_name=self.name
		self.name=new_name
		print old_name,'has been changed to-->',self.name
		
class text(basic):
	"""docstring for text"""
	def __init__(self,name,create_date,including,create_user_id):
		basic.__init__(self,name,create_date)
		self.user_id=create_user_id
		self.t=name
		self.incl=including
		print 'your text',self.t,'create success!'
class user(basic):
	"""docstring for user"""
	def __init__(self,name,create_date):
		basic.__init__(self,name,create_date)
		global user_num
		user_num=user_num+1
		self.user_id=user_num
	def change_username(self,newname):
		self.name=newname
		print 'user_id:',self.user_id,' change name-->',self.name
