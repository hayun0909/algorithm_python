from collections import defaultdict

N = int(input())
edge = int(input())
graph = defaultdict(list)
visited = [True] * (N+1)
cnt = 0

for i in range(edge):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for j in graph.keys():
    graph[j].sort()

def dfs(graph, v, visted):
    global cnt
    visited[v] = False
    cnt += 1
    for i in graph[v]:
        if visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)

print(cnt-1)
