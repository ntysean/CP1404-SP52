word_to_count = {}
text = str(input("input string to be counted here:"))
words = text.split()
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency +1
words = list(word_to_count.keys())
words.sort()


for word in words:
    print("{} : {}".format(word, word_to_count[word]))

