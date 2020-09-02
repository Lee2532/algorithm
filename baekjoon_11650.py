# https://www.acmicpc.net/problem/11650
# 좌표 정렬하기
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
# 정답

N = int(input())

result = []
for _ in range(N):
    result.append(list(map(int, input().split())))

result.sort(key = lambda x : (x[0], x[1]))
for i, j in result:
    print(i, j)
