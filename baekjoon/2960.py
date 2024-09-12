from collections import deque

N, K = input().split()
N, K = int(N), int(K)

num_list = [ i for i in range(2, N+1) ]
is_prime = [True] * (N+1)
cnt = 0

is_prime[0] = False
is_prime[1] = False

for i in range(2, len(is_prime)):
    if is_prime[i]:
        for j in range(i, len(is_prime), i):
            if is_prime[j]:
                is_prime[j] = False
                cnt += 1
            if cnt == K:
                print(j)
                break
    if cnt == K:
        break
