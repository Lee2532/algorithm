# https://www.acmicpc.net/problem/2108
# 통계학
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
# 산술평균, 중앙값, 최빈값, 범위
# 미완성


#산술평균
#N개의 수들의 합을 N으로 나눈값

def avg(N, list):
    return round(sum(list) / N)

def mid(N, list):
    list.sort()

    if N % 2 != 0: #짝수개.... 1, 2, 3, 4 있을떈 2+3의 중간값??
        mid = list[int(N/2)]
    else:
        mid = list[N/2]

    return mid

from collections import Counter
def many(N, list):
    result = Counter(list).most_common(2)

    return result


N = int(input())
list = []

for i in range(N):
    list.append(int(input()))

print(avg(N, list))
print(mid(N, list))
print(many(N, list))



