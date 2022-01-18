n = int(input('write down any number: '))
count_number = n
digits_count = 0
while n > 0:
    digits_count += 1
    n = n // 10
print(digits_count)