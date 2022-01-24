def sum_digits(x):
    return sum(map(int, x))
x = input()
middle = len(x) // 2
if middle == 0 or sum_digits(x[:middle]) == sum_digits(x[-middle:]):
    print('Lucky number')
else:
    print('common')