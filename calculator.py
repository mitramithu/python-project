# #1.calculator

choice=int(input('enter your choice:'))
if (choice>=1) and (choice<=4):
    print('enter two numbers:')
num1=int(input())
num2=int(input())

if choice==1:
    res=num1+num2
    print('result=',res)
elif choice==2:
    res=num1-num2
    print('result=',res)
elif choice==3:
    res=num1*num2
    print('result=',res)
elif choice==4:
    res=num1/num2
    print('result=',res)
elif choice==5:
    exit()
else:
    print()

## 2.calculator using functions

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

print('a.add')
print('b.subtract')
print('c.multiply')
print('d.divide')

choice=(input('enter your choice:'))
if (choice>='a') and (choice<='d'):
    print('enter numbers')

num1=int(input())
num2=int(input())

if choice=='a':
    print(num1+num2)
elif choice=='b':
    print(num1+num2)
elif choice=='c':
    print(num1*num2)
elif choice==d:
    print(num1/num2)
else:
    print('invalid')

