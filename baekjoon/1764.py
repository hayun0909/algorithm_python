N, M = map(int, input().split())

people_list = {}
cnt_list = []

for i in range(N+M):
    p = input()
    if p in people_list.keys():
        people_list[p] += 1
    else:
        people_list[p] = 1

for k, v in people_list.items():
    if v > 1:
        cnt_list.append(k)

cnt_list.sort()
print(len(cnt_list))
for cnt in cnt_list:
    print(cnt)

#### timeout error
# not_see = []
# not_listen = []
# not_see_listen = []

# for i in range(N):
#     not_see.append(input())

# for j in range(M):
#     not_listen.append(input())

# if N < M or N == M:
#     for see in not_see:
#         if see in not_listen:
#             not_see_listen.append(see)
# else:
#     for listen in not_listen:
#         if listen in not_see:
#             not_see_listen.append(listen)

# not_see_listen.sort()

# print(len(not_see_listen))
# for nsl in not_see_listen:
#     print(nsl)