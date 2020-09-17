# # 카카오 1번문제
#
# # import re
# #
# #
# # def dot_match(new_id):
# #     while True:
# #         if len(new_id) < 1:
# #             return new_id
# #         if new_id[0] == '.':
# #             new_id = new_id[1:]
# #         elif new_id[-1] == '.':
# #             new_id = new_id[:-1]
# #         else:
# #             return new_id
# #
# #
# # def solution(new_id):
# #     answer = ''
# #     # 1단계 소문자 변환
# #     new_id = new_id.lower()
# #     # 2단계 특수기호 제외
# #     new_id = "".join(re.findall(u'[a-z0-9\-\_\.]+', new_id))
# #
# #     # 3단계 ..이 2번이상이면 .으로 치환 #반복문
# #     while True:
# #         if '..' in new_id:
# #             new_id = new_id.replace('..', '.')
# #         else:
# #             break
# #     # 4단계 처음과 끝에 . 이 있으면 제거한다.
# #     new_id = dot_match(new_id)
# #     # 5단계 빈 문자열이라면 a를 대입한다
# #     if len(new_id) < 1:
# #         new_id = 'a'
# #     # 6단계 16자 이상이면 첫 15개 문자를 제외한 나머지 모두 제거하고나서 . 있으면 다시 반복
# #     if len(new_id) >= 16:
# #         new_id = new_id[:15]
# #     new_id = dot_match(new_id)
# #     # 7단계 2자 이하라면 마지막 문자를 붙이고 3자 이상될때까지~~
# #     while True:
# #         if len(new_id) < 3:
# #             new_id = new_id + new_id[-1]
# #         else:
# #             break
# #     return new_id
#
#
#
# #카카오 3번문제
# import json
#
#
# def make_dict(info):
#     result = []
#     lang = list(set([x.split()[0] for x in info]))
#     dev = list(set([x.split()[1] for x in info]))
#     career = list(set([x.split()[2] for x in info]))
#     food = list(set([x.split()[3] for x in info]))
#     score = [x.split()[4] for x in info]
#
#     # result_dict['lang'] = lang
#     # result_dict['dev'] = dev
#     # result_dict['career'] = career
#     # result_dict['food'] = food
#     # result_dict['score'] = score
#
#     page = {
#         'lang': {lang},
#         'dev': {dev : dev},
#         'career' : {career : career},
#         'food': {food : food},
#         'score': {score},
#     }
#     result.append(page)
#     return result
#
# def solution(info, query):
#     result = make_dict(info)
#     print(result)
#     # java and backend and junior and pizza 100
#     query = ["java and backend and junior and pizza 100"]
#
#
#     for i in query:
#         count = 0
#         for j in result[0].get('lang'):
#             if i.split()[0] == j: # 언어
#                 pass
#
#                 # if i.split()[2] == j:  # 직군
#                 #     if i.split()[4] == j:  # 경력
#                 #         if i.split()[6] == j:  # 음식
#                 #             if i.split()[8] == j:  # 점수
#                 #                 pass
#
#
#
#
#     # return answer
#
# if __name__ == '__main__':
#     info = ["java backend junior pizza 150",
#             "python frontend senior chicken 210",
#             "python frontend senior chicken 150",
#             "cpp backend senior pizza 260",
#             "java backend junior chicken 80",
#             "python backend senior chicken 50"]
#     query = [ "java and backend and junior and pizza 100",
#               "python and frontend and senior and chicken 200",
#             "cpp and - and senior and pizza 250",
#               "- and backend and senior and - 150",
#               "- and - and - and chicken 100",
#         "- and - and - and - 150"]
#
#     solution(info, query)
#


def solution(N):
    result = ''
    flag = True

    for i in str(N): #양수일 경우
        if int(i) <= 5 and flag == True:
            result += str(5)
            result += i
            flag = False
        else:
            result += i
    print(result)

if __name__ == '__main__':
    N = 268
    solution(N)