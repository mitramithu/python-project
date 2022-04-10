# #1.calculator
#
# choice=int(input('enter your choice:'))
# if (choice>=1) and (choice<=4):
#     print('enter two numbers:')
# num1=int(input())
# num2=int(input())
#
# if choice==1:
#     res=num1+num2
#     print('result=',res)
# elif choice==2:
#     res=num1-num2
#     print('result=',res)
# elif choice==3:
#     res=num1*num2
#     print('result=',res)
# elif choice==4:
#     res=num1/num2
#     print('result=',res)
# elif choice==5:
#     exit()
# else:
#     print()

## 2.calculator using functions

# def add(a,b):
#     return a+b
# def subtract(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def divide(a,b):
#     return a/b
#
# print('a.add')
# print('b.subtract')
# print('c.multiply')
# print('d.divide')
#
# choice=(input('enter your choice:'))
# if (choice>='a') and (choice<='d'):
#     print('enter numbers')
#
# num1=int(input())
# num2=int(input())
#
# if choice=='a':
#     print(num1+num2)
# elif choice=='b':
#     print(num1+num2)
# elif choice=='c':
#     print(num1*num2)
# elif choice==d:
#     print(num1/num2)
# else:
#     print('invalid')


## list methods

# fruits=['mango','kiwi','cherry']
# fruits.append('orange')
# print(fruits)

# flowers=['jasmine','lily','lotus']
# flowers.clear()
# print(flowers)

# numbers=[12,45,89,34]
# x=numbers.copy()
# print(x)

# fruits=['apple','mango','pomegranate']
# veg=['carrot','beetroot','tomato']
# fruits.extend(veg)
# print(fruits)

# names=['anu','dolu','bolu','zara']
# x=names.index('dolu')
# print(x)

# flowers=['jasmine','lily','lotus']
# flowers.insert(2,'rose')
# print(flowers)

# numbers=[12,45,89,34]
# numbers.pop()
# print(numbers)

# colors=['red','black','white','yellow']
# colors.remove('black')
# print(colors)

# fruits=['mango','banana','apple']
# fruits.reverse()
# print(fruits)

# numbers=[45,90,23,56]
# numbers.sort()
# print(numbers)

### dictionary methods

# dict={1:'anu',2:'zara',3:'vino'}
# dict.clear()
# print(dict)

# dict={1:'anu',2:'zara',3:'vino'}
# x=dict.copy()
# print(x)

# x={'apple','mango','guava'}
# y=1
# dict=dict.fromkeys(x,y)
# print(dict)

# car={1:'ford',2:'BMW',3:'benz'}
# x=car.get(2)
# print(x)

# x={1:'apple',2:'mango',3:'guava'}
# y=x.items()
# print(y)

# y={'fruit':'apple','flower':'lily'}
# x=y.keys()
# print(x)

# dict={1:'anu',2:'zara',3:'vino'}
# dict.pop(3)
# print(dict)

# y={'fruit':'apple','flower':'lily'}
# y.popitem()
# print(y)

# x={1:'apple',2:'mango',3:'guava'}
# y=x.setdefault(2,'kiwi')
# print(y)

# car={'brand':'ford','model':'mustang','year':1964}
# car.update({'color':'black'})
# print(car)

# y={'fruit':'apple','flower':'lily'}
# x=y.values()
# print(x)

## string methods

# text='hello,have a nice day'
# x=text.capitalize()
# print(x)

# text='Hello,have a nice day'
# x=text.casefold()
# print(x)

# text='hello'
# x=text.center(14)
# print(x)

# text='mango is my favourite fruit and it is yellow in colour'
# x=text.count('is')
# print(x)

# text='I am a doctor'
# x=text.encode()
# print(x)

# text='hello,have a nice day.'
# x=text.endswith('.')
# print(x)

# txt='h\te\tl\tl\to'
# x=txt.expandtabs(3)
# print(x)

# txt='for only {price:.3f} rupees'
# print(txt.format(price=80))

#text='hello,have a nice day'
# print(text.index('day'))

# text='rollno31'
# print(text.isalnum())

# text='hello,have a nice day'
# print(text.isascii())

# text='5.6'
# print(text.isdecimal())

# text='9000'
# print(text.isdigit())

# text='hello'
# print(text.isidentifier()

# text='hello,have a nice day'
# print(text.islower())

# text='5000'
# print(text.isnumeric())

# text='hello #2'
# print(text.isprintable())

# text='hello,Have a nice day'
# print(text.isupper())

# str1='mango','apple'
# print(','.join(str1))

# text='apple'
# x=text.ljust(15)
# print(x,'is a fruit')

# text='Hello EveryOne'
# print(text.lower())

# text='     lily   '
# x=text.lstrip()
# print('of all flowers',x,'is my favourite ''flower')

# text='hello pam'
# x=text.maketrans('p','s')
# print(text.translate(x))

# text='i like bananas than any other fruit'
# print(text.partition('bananas'))

# text='hello everyone, have a nice day'
# print(text.rfind('day'))

# text='hello, have a nice day'
# print(text.rindex('a'))

# text='i could eat bananas all day, bananas are my favourite fruit'
# print(text.rpartition('bananas'))

# text='lily, jasmine, rose'
# print(text.rsplit(','))

# text='hello, have a nice day'
# print(text.split())

# t='hello everyone\n have a nice day'
# print(t.splitlines())

# t='hello, have a nice day'
# print(t.startswith('hello'))

# text='   hello, have a nice day'
# print(text.strip())

# text='hello, have a nice day'
# print(text.swapcase())

# text='welcome to my world'
# print(text.title())

# d={83:80}
# text='hello sam'
#print(text.translate(d))

text='90'
print(text.zfill(5))