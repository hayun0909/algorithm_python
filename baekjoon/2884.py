H, M = map(int, input().split())

if M < 45:
    if H != 0:
        H -= 1
    else:
        H = 23
    M += 15 # 60 - 45
else:
    M = M - 45

print(H, M)