N = int(input())
cnt = 0
cnt += N//5  


n = N - cnt * 5

if n%3 != 0:
    k = 0
    for i in range(cnt, 0, -1):
        n = N - i * 5
        if n%3 == 0 :
            k = i + n//3
            print(k)
            break
    if k == 0:
        if N%3 == 0:
            print(N//3)
        else:
            print('-1')
else:
    cnt += n//3
    print(cnt)