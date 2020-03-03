from customer import customerList

c = customerList()

'''
for fn in c.fn1:
	var = input("Enter "+ fn + "\n")
	c.set(fn, var)
c.add()
#if c.verifyNew():
c.insert()
print(c.data)
#else:
print(c.errList)
c.getByField('fname','Anu')
print(c.data)

c.getLikeField('fname','anusuya')
print(c.data) 
'''

c.getFields()