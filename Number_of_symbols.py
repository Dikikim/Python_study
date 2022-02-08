x = input('write smth: ')

res = {}

for item in x:
    if res.get(item):
        res[item] += 1
    else:
        res[item] = 1

print(res)