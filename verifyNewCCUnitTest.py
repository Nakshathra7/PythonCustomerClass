from customer import customerList

cl = customerList()
#d = {'fname':'Anusuya','lname':'Manoharan','\
#email':'manoha@clarkson.edu','password':'123abc','subscribed':'1'}
#cl.add(d)
cl.set('fname','Saravanan')
cl.set('lname','')
cl.set('email','saranclarkson.edu')
cl.set('password','asdf')
cl.set('subscribed',1)

cl.add()

cl.set('fname','Anusuya')
cl.set('lname','Manoharan')
cl.set('email','manoha@clarkson.edu')
cl.set('password','rtrt123')
cl.set('subscribed',False)
cl.add()	

cl.verifyNew()
print(cl.errList)


