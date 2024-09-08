palindrome = []
while True:
    n = input()
    if int(n) == 0:
        break
    is_palin = True
    for i in range(len(n)//2):
        if n[i] != n[-1-i]:
            is_palin = False
    if is_palin:
        palindrome.append('yes')
    else:
        palindrome.append('no')

for palin in palindrome:
    print(palin)