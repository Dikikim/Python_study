sentence = input('write_something: ')
words = dict()

for word in sentence.split(' '):
    words[len(word)] = word

biggestWord = words[max(words)]
print(biggestWord)