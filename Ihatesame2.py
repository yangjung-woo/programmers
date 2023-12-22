
def solution(s):
    # 함수를 완성하세요
    a = []
    for i in s:
        if a[-1:] == [i]: # 현재 문자 i 와 가장 최근에 추가된 문자가 같으면 추가하지 않고 skip
            a_1 = a[-1]
            i_1 = [i]
            continue   # 뒤에서 부터 확인 
        # 현재 문자와 마지막 문자가 다르다면 answer 추가
        a.append(i)
    return a

arr =[1,1,3,3,0,1,1]	

print(solution(arr))