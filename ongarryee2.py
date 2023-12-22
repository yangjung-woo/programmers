
can_say =['aya', 'ye', 'woo', 'ma']
def solution(babbling):
    
    answer = 0
    for word in babbling:
        cnt =0
        say =''
        for a in word:
            say +=a
            if say in can_say:
                say =''
                cnt+=1
        if len(say) ==0 and cnt > 0:
            answer += 1
    
    return answer