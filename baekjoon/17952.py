import sys; input = sys.stdin.readline

N = int(input())

A_list = []
T_list = []
score = 0

for i in range(N):
    a = input().split()
    if int(a[0]):
        A_list.append(int(a[1]))
        T_list.append(int(a[2]))
    if T_list != []:
        T_list[-1] -= 1
    if T_list != [] and T_list[-1] == 0:
        T_list.pop()
        score += A_list.pop()

print(score)