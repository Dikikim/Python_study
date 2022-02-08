days = {
     1: 'Monday',
     2: 'Tuesday',
     3: 'Wednesday',
     4: 'Thursday',
     5: 'Friday',
     6: 'Saturday',
     7: 'Sunday'
}
x = 0
while (x < 1) or (x > 7): x = int(input('write number of a day: '))
print(days[x])