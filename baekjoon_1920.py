# https://www.acmicpc.net/problem/1920
# 수 찾기
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
# 정답

N = input()
N_list = sorted(map(int,input().split()))
M = input()
M_list = map(int, input().split()) # 이부분도 sort해서 틀림

def binary(i, N_list, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if i == N_list[m]:
        return 1
    elif i < N_list[m]:
        return binary(i, N_list, start, m-1)
    else:
        return binary(i, N_list, m+1, end)

for i in M_list:
    start = 0
    end = len(N_list)-1
    print(binary(i, N_list, start, end))