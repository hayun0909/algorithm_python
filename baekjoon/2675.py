T = int(input())
arr = []
for i in range(T):
    R, P = input().split()
    R = int(R)
    array = []
    for p in P:
        array.append(R * p)
    j = ''.join(array)
    arr.append(j)
for k in range(len(arr)):
    print(arr[k])