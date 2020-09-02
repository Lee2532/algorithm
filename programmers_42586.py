#https://programmers.co.kr/learn/courses/30/lessons/42586


def solution(progresses, speeds):
    answer = []
    while len(progresses) != 0:
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]

        if progresses[0] > 99:
            count = 0
            while progresses[0] > 99:
                count += 1
                progresses.pop(0)
                speeds.pop(0)
                if len(progresses) == 0:
                    break
            answer.append(count)
    return answer




if __name__ == '__main__':
    progresses = [93, 30, 55]
    speeds= [1, 30, 5]

    print(solution(progresses, speeds))