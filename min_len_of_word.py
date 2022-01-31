sentence = input('write_something: ')
words = dict()

for word in sentence.split(' '):
    words[len(word)] = word

shortestWord = words[min(words)]
print(shortestWord)