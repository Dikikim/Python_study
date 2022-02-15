b = []
d = {}
for x in range(999, 99, -1):
    for y in range(x, 99, -1):
        s = str(x * y)
        c = s[::-1]
        if s == c:
            b.append(s)
            d[s] = (x, y)
a = max(b)
print(d[a])
print(a)

