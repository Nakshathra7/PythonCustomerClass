import pymysql

class customerList:
	def __init__(self):
		self.data = []
		self.tempdata = {}
		self.tn = 'customers'
		self.fn1 = ['fname', 'lname', 'email', 'password', 'subscribed']
		self.errList = ['empty','emailcheck','subscribedchk','passwordlen']
		self.conn = None

	def connect(self):
		#return pymysql.connect(host='mysql.clarksonmsda.org',port=3306,user='manoha',password='is437clarkson',db='manoha_is437',autocommit=True)

		self.conn = pymysql.connect(host='mysql.clarksonmsda.org',port=3306,user='manoha',password='is437clarkson',db='manoha_is437',autocommit=True)

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

	#def verifyNew(self,validate):
		#if tempdata == ''



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







