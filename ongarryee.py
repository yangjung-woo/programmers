# 옹알이 문제 

can_say = ["aya", "ye", "woo", "ma"]

def solution(babbling):
    answer = 0
    for word in babbling:
        s = ''
    
        for alpha in word:
            s += alpha
            if s in can_say:
                s =''
                cnt +=1
        if len(s) ==0 and cnt >0:
            answer += 1


    return answer