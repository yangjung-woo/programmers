# 저주의 숫자 3
# 1 2 3 4 5 6 7 8 9 10  # 10진수
# 1 2 4 5 7 8 10 11 13 16   // 저주받은 마을의 숫자 
# 절대 3의 배수 숫자를 사용하지 않는다 


def solution(n):
    answer = 0
    for i in range (n):
        answer+=1
        while answer%3 ==0 or '3' in str(answer):
            answer+=1
    return answer