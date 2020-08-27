#https://programmers.co.kr/learn/courses/30/lessons/42626

from collections import defaultdict
import heapq


def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    while True:
        if heap[0] >= K:
            return answer
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
            answer += 1
            if heap[0] >= K:
                return answer
        except:
            return -1

# def solution(scoville, K):
#     heap = []
#     for i in scoville:
#         heapq.heappush(heap, i)
#     count = 0
#
#     while True:
#         try:
#             count += 1
#             new_scoville = heapq.heappop(heap) + (heapq.heappop(heap) * 2)
#             if new_scoville > K:
#                 return count
#             heapq.heappush(heap, new_scoville)
#
#         except:
#             return -1


if __name__ == '__main__':
    scoville = 	[1, 2, 3, 9, 10, 12]
    K = 7
    print(solution(scoville, K))
    # print(solution(scoville, K))