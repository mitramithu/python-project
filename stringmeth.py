
## string methods

text='hello,have a nice day'
x=text.capitalize()
print(x)

text='Hello,have a nice day'
x=text.casefold()
print(x)

text='hello'
x=text.center(14)
print(x)

text='mango is my favourite fruit and it is yellow in colour'
x=text.count('is')
print(x)

text='I am a doctor'
x=text.encode()
print(x)

text='hello,have a nice day.'
x=text.endswith('.')
print(x)

txt='h\te\tl\tl\to'
x=txt.expandtabs(3)
print(x)

txt='for only {price:.3f} rupees'
print(txt.format(price=80))

text='hello,have a nice day'
print(text.index('day'))

text='rollno31'
print(text.isalnum())

text='hello,have a nice day'
print(text.isascii())

text='5.6'
print(text.isdecimal())

text='9000'
print(text.isdigit())

text='hello'
print(text.isidentifier()

text='hello,have a nice day'
print(text.islower())

text='5000'
print(text.isnumeric())

text='hello #2'
print(text.isprintable())

text='hello,Have a nice day'
print(text.isupper())

str1='mango','apple'
print(','.join(str1))

text='apple'
x=text.ljust(15)
print(x,'is a fruit')

text='Hello EveryOne'
print(text.lower())

text='     lily   '
x=text.lstrip()
print('of all flowers',x,'is my favourite ''flower')

text='hello pam'
x=text.maketrans('p','s')
print(text.translate(x))

text='i like bananas than any other fruit'
print(text.partition('bananas'))

text='hello everyone, have a nice day'
print(text.rfind('day'))

text='hello, have a nice day'
print(text.rindex('a'))

text='i could eat bananas all day, bananas are my favourite fruit'
print(text.rpartition('bananas'))

text='lily, jasmine, rose'
print(text.rsplit(','))

text='hello, have a nice day'
print(text.split())

t='hello everyone\n have a nice day'
print(t.splitlines())

t='hello, have a nice day'
print(t.startswith('hello'))

text='   hello, have a nice day'
print(text.strip())

text='hello, have a nice day'
print(text.swapcase())

text='welcome to my world'
print(text.title())

d={83:80}
text='hello sam'
print(text.translate(d))

text='90'
print(text.zfill(5))