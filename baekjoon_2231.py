#https://www.acmicpc.net/problem/2231
# 정답

N = int(input())

answer = []
for i in reversed(range(N)):
    result = i

    for j in str(i):
        result += int(j)

    if result == N:
        answer.append(i)
answer.sort()
if len(answer) < 1:
    print(0)
else:
    print(answer[0])