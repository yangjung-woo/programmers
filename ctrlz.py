def solution(s):
    
    temp = list(s.split())
    temp.reverse()
    answer = 0
    flag = False
    for t in temp:
        if t =='Z':
            flag = True
            continue
        if flag:
            flag=False
            continue
        if flag == False:
            answer+= int(t)
    
    return answer



s = "10 Z 20 Z 1"
print(solution(s))