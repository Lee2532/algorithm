# https://www.acmicpc.net/problem/1436
# 정답

N = int(input()) # N번째 영화의 제목에 들어간 수를 출력한다.

x = 665

while N:                        # N번만큼 반복
    x += 1
    if '666' in str(x):         # x에 666이 있다면
        N -= 1
print(x)