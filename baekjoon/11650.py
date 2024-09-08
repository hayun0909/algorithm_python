N = int(input())
coordinate_list = []

for i in range(N):
    x, y = input().split()
    x, y = int(x), int(y)
    coordinate_list.append((x, y))

coordinate_list.sort()

for x, y in coordinate_list:
    print(x, y)