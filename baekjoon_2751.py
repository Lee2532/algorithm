#https://www.acmicpc.net/problem/2751
#시간초과로 인해 실패


N = input()

result = []
for i in range(int(N)):
    result.append(input())
result.sort()
for i in result:
    print(i)