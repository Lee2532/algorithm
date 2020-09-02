# https://www.acmicpc.net/problem/13702
# 이상한 술집
# 첫째 줄에는 은상이가 주문한 막걸리 주전자의 개수 N, 그리고 은상이를 포함한 친구들 K명이 입력된다. N은 10000이하의 정수이고, K는 1,000,000이하의 정수이다. 막걸리의 용량은 231 -1 보다 작거나 같은 자연수 또는 0이다. 단, 항상 N ≤ K 이다. 즉, 주전자의 개수가 사람 수보다 많을 수는 없다.
# ??? 왜 틀리는거냐,,,

N, K = map(int, input().split())

volume = []
for i in range(N):
    volume.append(int(input()))

volume.sort()
answer = []

for i in reversed(range(volume[0] + 1)):
    if i == 0:
        print(0)
        break
    result = 0
    for j in volume:
        result += (j // i)
    if result == K:
        print(i)
        break
