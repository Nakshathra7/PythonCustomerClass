import pymysql
import re
from baseObject import baseObject

class productList(baseObject):
	def __init__(self):
		self.setupObject('products')

	def verifyNew(self,n=0):
		self.errList = []

		if len(self.data[n]['sku']) == 0:
			self.errList.append("SKU cannot be blank")

		if len(self.data[n]['name']) == 0:
			self.errList.append("Name cannot be blank")

		if len(self.data[n]['price']) == 0:
			self.errList.append("Price cannot be blank")

		#if len(self.data[n]['price']) < 0:
		#	self.errList.append("Price should have value")

		if len(self.errList) > 0:
			return False
		else:
			return True	

		#Add if statements for validation of other fields
		#Add Unit Test






