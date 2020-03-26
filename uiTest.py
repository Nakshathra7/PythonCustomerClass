from customer import customerList

cl = customerList()

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

#c.getFields()

print(cl.fn1)
print(cl.pk)

cl.set('fname','Anusuya')
cl.set('lname','Manoharan')
cl.set('email','saran@clarkson.edu')
cl.set('password','abc123')
cl.set('subscribed',True)	
cl.add()

cl.insert()

c = customerList()
c.getAll()
print(c.data)