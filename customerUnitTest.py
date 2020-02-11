from customer import customerList

cl = customerList()
#d = {'fname':'Anusuya','lname':'Manoharan','\
#email':'manoha@clarkson.edu','password':'123abc','subscribed':'1'}
#cl.add(d)
cl.set('fname','Saravanan')
cl.set('lname','Manoharan')
#cl.set('lastname','Manoharan')
cl.set('email','saran@clarkson.edu')
cl.set('password','abc123')
cl.set('subscribed',True)	
cl.add()	
cl.add()
print(cl.data)
print(cl.data[0])
#print(cl.data[0].['email'])
#print(cl.data[0].['email']) = dfdf@sdsdf.com
cl.update(0,'email','errere@fgfdfd.com')
#print(cl.data[0].email)
#print(cl.data)

cl.insert()

#INSERT INTO `customers` (`fname`,`lname`,`email`,`password`,`subscribed`) VALUES (%s,%s,%s,%s,%s);
#pip3 install pymysql
#python3 -m pip install pymysql

