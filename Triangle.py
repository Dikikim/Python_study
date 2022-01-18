print("write down triangle's sides")
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
p = (a+b+c)/2
S = (p*(p-a)*(p-b)*(p-c))**0.5
print('S =', S)