# https://www.acmicpc.net/problem/7568
# 정답

N = int(input()) # 전체 사람 수

person = []

for _ in range(N):
    height, weight = map(int, input().split()) # 키, 몸무게
    person.append((height, weight))

#result = sorted(person, key=lambda x: (x[0], x[1]), reverse=True) # 이렇게 하니 정답 출력이 힘듬

for p in person:
    rank = 1
    for n in person:
        if (p[0] < n[0]) and (p[1] < n[1]): # 각각 더 크면 rank +=1
                rank += 1
    print(rank, end=' ')