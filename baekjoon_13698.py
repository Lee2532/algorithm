# https://www.acmicpc.net/problem/13698
# Hawk eyes
# 첫째 줄에 재열이가 컵을 섞는 순서가 주어진다. 이 순서는 위 그림에 있는 A, B, C, D, E, F 중 하나이다. 재열이는 컵을 최대 200번 섞는다.
# 큰공 작은공 구분을 해야해서 틀렸었음,,,
# 정답



string = input()
list = list(range(4))

for i in string:
    if i == "A":
        list[0], list[1] = list[1], list[0]
    elif i == "B":
        list[0], list[2] = list[2], list[0]
    elif i == "C":
        list[0], list[3] = list[3], list[0]
    elif i == "D":
        list[1], list[2] = list[2], list[1]
    elif i == "E":
        list[1], list[3] = list[3], list[1]
    elif i == "F":
        list[2], list[3] = list[3], list[2]

print(list.index(0) + 1)
print(list.index(3) + 1)
