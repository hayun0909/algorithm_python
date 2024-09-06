from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs (graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        # print element in queue
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M, V = input().split()
N, M, V = int(N), int(M), int(V)
graph = []
# set graph
for n in range(N+1): # set index num
    graph.append([])
# construct graph
for i in range(M):
    main_node, link_node = input().split()
    main_node, link_node = int(main_node), int(link_node)
    graph[main_node].append(link_node)
    graph[link_node].append(main_node)

for j in range(len(graph)):
    graph[j].sort()

dfs(graph, V, [False]*(N+1))
print('')
bfs(graph, V, [False]*(N+1))