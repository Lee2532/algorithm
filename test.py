def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


from collections import  deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        # popleft 1 2 3 8 7 4 5 6
        # pop 1 8 7 6 3 5 4 2
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [[], [1, 2], [2, 3], [1, 5], [5, 2], [5, 6], [4, 7]]

visited = [False] * 9
dfs(graph, 1, visited)
visited = [False] * 9
bfs(graph, 1, visited)