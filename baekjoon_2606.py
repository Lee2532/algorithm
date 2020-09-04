# https://www.acmicpc.net/problem/2606
# 바이러스
# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
# 실패

def dfs(graph, v, visited):
    visited[v] = True
    # print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


computer = int(input()) # 컴퓨터 수
conn = int(input()) # 컴퓨터가 연결된 리스트

graph = [[] for _ in range(conn + 1)]
for i in range(1, conn+1):
    a, b = (list(map(int, input().split())))
    graph[a].append(b)


visited = [False] * (computer + 1)

dfs(graph, 1, visited)

count = 0
for i in visited:
    if i == True:
        count += 1

print(count -1)

'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7


7
7
1 2
2 3
1 5
5 2
5 6
4 7
1 3

'''
