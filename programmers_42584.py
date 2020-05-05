#https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []

    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                count +=1
            if prices[i] > prices[j]:
                count += 1
                break
        answer.append(count)
    return answer
