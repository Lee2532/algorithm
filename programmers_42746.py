from collections import defaultdict
#https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))



if __name__ == '__main__':
    numbers = [3, 30, 34, 5, 9]
    print(solution(numbers))