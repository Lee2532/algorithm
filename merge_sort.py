def merge_sort(xs, func='up'): #default 오름차순(up), down
    xss = [ [x] for x in xs ] # 리스트 조건제시법 list comperehension
    [ss] = msort(xss, func)
    return ss

def msort(xss, func): # bottom-up이라 알고리즘 정의대로 작성하면 자연스럽게 꼬리재귀가 된다
    if len(xss) > 1:
        return msort( [ merge(xss[i],xss[i+1], func) if i+1 < len(xss) else xss[i]
                          for i in range(0,len(xss),2) ], func)
    else:
        return xss

def merge(left,right,func): # 실습 5.9: merge 함수 while 버전
    ss = []
    while not (left == [] or right == []):
        if func == 'up':
            if left[0] <= right[0]:
                ss.append( left[0] )  # 끝에 원소 하나 붙이기
                left = left[1:]
            else:
                ss.append( right[0] ) # 끝에 원소 하나 붙이기
                right = right[1:]
        else:
            if left[0] <= right[0]:
                ss.append( right[0] )  # 끝에 원소 하나 붙이기
                right = right[1:]
            else:
                ss.append( left[0] ) # 끝에 원소 하나 붙이기
                left = left[1:]

    ss.extend(left)  # 끝에 리스트 연장
    ss.extend(right) # 끝에 리스트 연장
    return ss

print(merge_sort([ [4], [2], [1], [3] ], func='up'))
sorted([1,2,3,4,5], reverse=True)