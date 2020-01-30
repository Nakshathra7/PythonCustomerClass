class customerList:
	def __init__(self):
		self.data = []
		self.fn1 = ['fname', 'lname', 'email', 'password', 'subscribed']
	def add(self, item):
		self.data.append(item)