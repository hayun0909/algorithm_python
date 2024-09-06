S = input()
asci = 97 # a ASCII code num
pos = [-1] * 26
for i, s in enumerate(S):
    j = ord(s)-asci
    if pos[j] == -1:
        pos[j] = i
    else:
        pass
for k, p in enumerate(pos):
    if k == len(pos)-1:
        print(p)
    else:
        print(p, end=' ')