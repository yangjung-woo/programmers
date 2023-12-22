def solution(X, Y):
    # 공통으로 나타나는 정수들을 사용하여 만들수 있는 가장 큰 정수
    # 단 서로 짝 지을수 있ㅇㅇ 함 
    # 짝이 존재하지 않으면 -1 
    pair_list = []
    for x1 in X:
        for y1 in Y:
            if x1==y1:
                pair_list.append(y1)
    
    answer = ''
    return answer


X= "100"
Y = "203045"

print(solution(X,Y))