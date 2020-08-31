# https://www.acmicpc.net/problem/1181
# 단어 정렬
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 정답

N = int(input()) # 단어 수
result = []

for _ in range(N):
    result.append(input())
result = list(set(result)) # 중복제거
result.sort(key=lambda x : (len(x), x)) #길이, 단어 순으로 정렬
for i in result:
    print(i)