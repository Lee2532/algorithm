# https://www.acmicpc.net/problem/1260
# DFS와 BFS
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
# 실패

from collections import  deque

N, M, V = map(int, input().split()) #정점수, 간선의 개수, 시작할 번호

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


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


graph = [[] for _ in range(M+1)]
for i in range(1, M):
    a, b = map(int, input().split())
    graph[i].append(a)
    graph[i].append(b)

visited = [False] * (N + 1) # 방문여부
dfs(graph, V, visited) #그래프, 방문여부, 시작점
visited = [False] * (N + 1) # 방문여부
print()
bfs(graph, V, visited)

