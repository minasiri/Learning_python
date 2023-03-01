a="broadway"
print(a)
b = ''
print(b)
print(bool(''))
print(bool('HelloWorld'))
str1 = "hello world"
print(str1)
x = slice(2,5)
print(x)
len('')
print(len(''))

str1 = "Hello World"
print(str1.capitalize())
print(str1.upper())
print(str1.lower())
print(str1.title())


str1 = "Cookie cutter"
str2 = "cut"
str3 = "Cut"
print(str1.find(str2))
print(str1.find(str3))

str1 = 'hip hip hurray!'
print(str1.replace('hip','Hip'))
print(str1.replace('hip','Hip',1))

str1 = 'hello world'
print(str1.split())

pets= 'cat,dog,mouse'
print(pets.split(','))

str_lst = ['Hello', 'World']
print(''.join(str_lst))

pets = ['cat','dog','mouse']
print(','.join(pets))
print('','',''.join(pets))
print(''.join(pets))

a ="broadway"
messg = f"I study at {a}."
print(messg)

print('I am %s and I am %d years old'%('John Doe',23))

print('I am {} and I am {} years old.'.format('John Doe',23))

print('I have {1}, {0}, and {2} in my bag.'.format('book','pen','copy'))

print('{a},{b},{c}'.format(a='foo',b='bar',c='baz'))

name = "John Doe"
print(f"Hi! {name}")

#Braces
print("Braces")
print(f"{{2+3}}")
print(f"{2+3}")
print(f"{{{2+3}}}")