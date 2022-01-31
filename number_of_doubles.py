x = input()
y = {}
for i in x:
    if i in y:
        y[i] += 1
    else:
        y[i] = 1
print(y)
