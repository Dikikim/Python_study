x = int(input('input x: '))
y = str(x)
z = len(y)
for i in range(z//2):
    if y[i] != y[-1-i]:
       print("It isn't palindrome")
       break
else:
    print("It's palindrome")