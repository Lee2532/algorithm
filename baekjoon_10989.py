# https://www.acmicpc.net/problem/10989
# 수 정렬하기 3
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 정답

'''
#메모리 초과
N = int(input())

result = []
for _ in range(N):
    result.append(int(input()))
result.sort()
print(result)
'''

'''
#메모리 초과
import heapq
import sys

N = int(input())

result = []
for _ in range(N):
    heapq.heappush(result, int(sys.stdin.readline()))

print(result)

'''



import sys
N = int(input())
result = [0] * 10001

for i in range(N):
    number = int(sys.stdin.readline())
    result[number] = result[number] + 1

for i in range(len(result)):
    if result[i] !=0:
        for _ in range(result[i]):
            print(i)