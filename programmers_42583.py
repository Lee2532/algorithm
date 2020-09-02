# #https://programmers.co.kr/learn/courses/30/lessons/42583
#
#
# # def solution(bridge_length, weight, truck_weights):
# #     time = 0
# #     queue = [0] * bridge_length
# #
# #     while queue:
# #         time += 1
# #         queue.pop(0)
# #         if truck_weights:
# #             if sum(queue) + truck_weights[0] <= weight:
# #               #sum으로 인한 시간 out
# #                 queue.append(truck_weights.pop(0))
# #             else:
# #                 queue.append(0)
# #
# #     return time
#
#
# def solution(bridge_length, weight, truck_weights):
#     time = 0
#     queue = [0] * bridge_length
#
#     while queue:
#         time += 1
#         queue.pop(0)
#         if truck_weights:
#             if sum(queue) + truck_weights[0] <= weight:
#                 queue.append(truck_weights.pop(0))
#             else:
#                 queue.append(0)
#
#     return time
#
#
# if __name__ == '__main__':
#     bridge_length = 10
#     weight = 10
#     truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
#     print(solution(bridge_length, weight, truck_weights))



