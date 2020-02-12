import pymysql
import re

class customerList:
	def __init__(self):
		self.data = []
		self.tempdata = {}
		self.tn = 'customers'
		self.fn1 = ['fname', 'lname', 'email', 'password', 'subscribed']
		self.errList = []
		self.conn = None
		self.regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

	def connect(self):
		#return pymysql.connect(host='',port=3306,user='',password='',db='',autocommit=True)
		import config
		self.conn = pymysql.connect(host=config.DB['host'],port=config.DB['port'],user=config.DB['user'],password=config.DB['password'],db=config.DB['db'],autocommit=True)
		#self.conn = pymysql.connect(host='',port=3306,user='',password='',db='',autocommit=True)

	def add(self):
		#if len(self.tempdata) == len(self.fn1):
		self.data.append(self.tempdata)
	def set(self,fn, val):
		if fn in self.fn1:
			self.tempdata[fn] = val
		else:
			print('Invalid Field: ' + str(fn))
	def update(self,n,fn,val):
		if len(self.data) >= (n + 1) and fn in self.fn1:
			self.data[n][fn] = val
		else:
			print("Could not set value at row ",str(n),' col ', str(fn))

	def verifyNew(self,n=0):
		self.errList = []

		if len(self.data[n]['fname']) == 0:
			self.errList.append("First name cannot be blank")

		if len(self.data[n]['lname']) == 0:
			self.errList.append("Last name cannot be blank")

		if len(self.data[n]['email']) == 0:
			self.errList.append("Email cannot be blank")

		elif not(bool(re.search(self.regex,self.data[n]['email']))):
			self.errList.append("Enter Valid Email with . and @")

		if len(self.data[n]['password']) == 0:
			self.errList.append("Password cannot be blank")

		elif len(self.data[n]['password']) <= 4:
			self.errList.append("Password must be longer than 4 characters")

		if len(str(self.data[n]['subscribed'])) == 0:
			self.errList.append("Subscribed cannot be blank")

		elif type(self.data[n]['subscribed']) != bool:
			self.errList.append("Subscribed value must be 'True' or 'False'")

		if len(self.errList) > 0:
			return False
		else:
			return True	

		#Add if statements for validation of other fields
		#Add Unit Test

		

	def insert(self, n=0):
		
		cols = '`,`'.join(self.fn1)
		cols = '`'+cols+'`'
		vals = ('%s,'*len(self.fn1))[:-1]
		tokens = []
		for fieldname in self.fn1:
			tokens.append(self.data[n][fieldname])

		sql='INSERT INTO `' + self.tn + '` (' +cols+ ') VALUES (' + vals +');'
		#conn = self.connect()
		self.connect()
		#cur = conn.cursor(pymysql.cursors.DictCursor)
		cur = self.conn.cursor(pymysql.cursors.DictCursor)
		print(sql)
		print(tokens)
		cur.execute(sql,tokens)







