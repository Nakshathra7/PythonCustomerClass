from customer import customerList

cl = customerList()
#d = {'fname':'Anusuya','lname':'Manoharan','\
#email':'manoha@clarkson.edu','password':'123abc','subscribed':'1'}
#cl.add(d)
cl.set('fname','Anusuya')
cl.set('lname','Manoharan')
#cl.set('lastname','Manoharan')
cl.set('email','manoha@clarkson.edu')
cl.set('password','123abc')
cl.set('subscribed',True)	
cl.add()	
cl.add()
print(cl.data)
print(cl.data[0])
#print(cl.data[0].['email'])
#print(cl.data[0].['email']) = dfdf@sdsdf.com
cl.update(0,'email','dfd@fgfdfd.com')
#print(cl.data[0].email)
#print(cl.data)

cl.insert()

#INSERT INTO `customers` (`fname`,`lname`,`email`,`password`,`subscribed`) VALUES (%s,%s,%s,%s,%s);
#pip3 install pymysql
#python3 -m pip install pymysql

