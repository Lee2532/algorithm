# https://www.acmicpc.net/problem/10828
# 스택
# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 정답


N = int(input())

result = []
for _ in range(N):
    result.append(input())

stack = []

for i in result:
    i = i.split()
    if i[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif i[0] == 'push':
        stack.append(i[1])
    elif i[0] == 'size':
        print(len(stack))
    elif i[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif i[0] == 'top':
        if len(stack) < 1:
            print(-1)
        else:
            print(stack[len(stack)-1])

