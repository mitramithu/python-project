# accessing the values of dictionary inside a list

#list=[{'yellow':'marigold','white':'lily'},{'red':'apple','yellow':'mango'}]
#1.
# list[0]['white']='jasmine'
# list[1]['yellow']='papaya'
# print(list)

#2. using loop
# for d in list:
#     for key in d:
#         print (d[key])

# for d in list:
#     for values in d:
#         print(d[values])

###

# accessing the values of list inside dictionary

# country={'India':['tamil nadu','kerala'],'united states':['new york','texas']}
# print(country['India'])
# print(country['India'][0])
# print(country['united states'][1])

# adding values to tuple

# tuple=(1,2)
# list=list(tuple)
# list.append(3)
# tuple=tuple(list)
# print(tuple)

tuple=(1,2,3,4)
tuple=tuple+(12,)
print(tuple)

### printing the pattern using for loop

#n=int(input('enter number of rows:'))
# for i in range(n,0,-1):
#     for j in range(n,i,-1):
#         print(end=' ')
#     for k in range(0,i):
#         print('* ',end='')
#     print()
# for i in range(1,n):
#     for j in range(0,n-i-1):
#         print(end=' ')
#     for k in range(0,i+1):
#         print('* ',end='')
#     print()

### using while loop

# n=int(input('enter number of rows:'))
# i=n
# while i>1:
#     print(' '*(n-i)+'* '*i)
#     i-=1
# i=1
# while i<=n:
#     print(' '*(n-i)+'* '*i)
#     i+=1
