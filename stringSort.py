# 문자열 내림차순으로 배치하기
# 특히 sort( ) 함수의 리턴값이 None 이므로 주의합니다. 
# 정렬된 값은 리턴되지 않습니다. 



def solution(s):
    # 중요 포인트  문자열은 정렬 할 때 sorted(... )를 사용하라
    # list .sort() 는 리턴되지 않습니다. 
    new_s = sorted(s,reverse=True)
    answer =''.join(new_s) # 문자 혹은 숫자로 이루어진 리스트들을 합침 

    return answer

s = "Zbcdefg"

print(solution(s))