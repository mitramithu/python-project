### printing the pattern using for loop

n=int(input('enter number of rows:'))
for i in range(n,0,-1):
    for j in range(n,i,-1):
        print(end=' ')
    for k in range(0,i):
        print('* ',end='')
    print()
for i in range(1,n):
    for j in range(0,n-i-1):
        print(end=' ')
    for k in range(0,i+1):
        print('* ',end='')
    print()

### using while loop

n=int(input('enter number of rows:'))
i=n
while i>1:
    print(' '*(n-i)+'* '*i)
    i-=1
i=1
while i<=n:
    print(' '*(n-i)+'* '*i)
    i+=1
