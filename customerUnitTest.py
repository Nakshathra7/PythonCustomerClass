from customer import customerList

cl = customerList()
d = {'fname':'Anusuya','lname':'Manoharan','\
email':'manoha@clarkson.edu','password':'123abc','subscribed':'1'}
cl.add(d)
print(cl.data)