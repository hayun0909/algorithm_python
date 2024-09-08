N = int(input())
words = []
for i in range(N):
    word = input()
    if word not in words:
        words.append(word)

# words = sorted(words, key=lambda x:(x[0], len(x))) # can possible for one line

words.sort()
words = sorted(words, key=lambda x: len(x))

for w in words:
    print(w)