#https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = [0, 0, 0]
    number_1 = [1, 2, 3, 4, 5]
    number_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    number_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i, j in enumerate(answers):
        if number_1[i % len(number_1)] == j:
            answer[0] += 1
        if number_2[i % len(number_2)] == j:
            answer[1] += 1
        if number_3[i % len(number_3)] == j:
            answer[2] += 1

    return [i + 1 for i, j in enumerate(answer) if j == max(answer)]