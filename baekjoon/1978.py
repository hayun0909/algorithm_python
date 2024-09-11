N = int(input())
num = input().split()
num = [ int(n) for n in num ]
cnt = 0

num_list = [ i for i in range(2, 1000+1) ]
is_prime = [True] * 1001

is_prime[0] = False
is_prime[1] = False

for i in range(2, len(is_prime)):
    if is_prime[i]:
        # for j in range(i + i, len(is_prime), i):
            # is_prime[j] = False
        for j in range(2, int((len(is_prime))/i) + 1):
            if i * j < len(is_prime):
                is_prime[i*j] = False

for n in num:
    if is_prime[n]:
        cnt+=1

print(cnt)