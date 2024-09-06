N = int(input())
arr = []
for i in range(N):
    n = int(input())
    arr.append(n)
arr.sort()
for j in range(N):
    print(arr[j])