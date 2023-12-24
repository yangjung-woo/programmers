
'''
# 생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 

예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다.

즉, 해당 학생은 여벌 체육복을 가지고 있지만 동시에 잃어버리기도 한 것이니 
lost와 reserve 둘 다 포함이 된단 뜻이며, 체육 수업을 들을 수 있는 학생이므로 미리 제외를 시켜줘야한다.

 ex) lost=[1,3,5] reserve=[3,4,7] 일 경우, 3번 학생이 여벌 체육복을 갖고있으면서 잃어버린 상황에 해당 한다.
'''
def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    for i in new_lost:
        if i + 1 in new_reserve:
            new_reserve.remove(i + 1)
        elif i - 1 in new_reserve:
            new_reserve.remove(i - 1)
        else:
            n-=1
    return n


print(solution(5, [2, 4],[1, 3, 5]))