### dictionary methods

dict={1:'anu',2:'zara',3:'vino'}
dict.clear()
print(dict)

dict={1:'anu',2:'zara',3:'vino'}
x=dict.copy()
print(x)

x={'apple','mango','guava'}
y=1
dict=dict.fromkeys(x,y)
print(dict)

car={1:'ford',2:'BMW',3:'benz'}
x=car.get(2)
print(x)

x={1:'apple',2:'mango',3:'guava'}
y=x.items()
print(y)

y={'fruit':'apple','flower':'lily'}
x=y.keys()
print(x)

dict={1:'anu',2:'zara',3:'vino'}
dict.pop(3)
print(dict)

y={'fruit':'apple','flower':'lily'}
y.popitem()
print(y)

x={1:'apple',2:'mango',3:'guava'}
y=x.setdefault(2,'kiwi')
print(y)

car={'brand':'ford','model':'mustang','year':1964}
car.update({'color':'black'})
print(car)

y={'fruit':'apple','flower':'lily'}
x=y.values()
print(x)

