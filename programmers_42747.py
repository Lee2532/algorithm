from collections import defaultdict
#https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort()

    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            return len(citations) - i
    return 0


    # print(l)
    # for i in range(l):
    #     if citations[i] >= l-i:
    #         # 논문이 인용된 횟수(h번 이상) >= 인용된 논문의 개수(h개 == h번)
    #         return l-i
    # return 0


if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    # citations = [31, 66]
    print(solution(citations))