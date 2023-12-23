#1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
#2. words에 있는 단어로만 변환할 수 있습니다.

# 가장 짧은 최단 거리를 구하는 것이기 때문에 answer =1000
# 단어가 하나만 다르면 연결되어있음 

answer =10000
def connect_check(begin, target):
    wl = len(begin)  # begin 과 target 은 같은 단어수 
    diff = 0
    s1 = list(begin)
    s2 = list(target)
    for i in range(wl):
        if s1[i] != s2[i]:
            diff +=1
    if diff ==1:
        return True
    else:
        return False

def dfs(now,target,cnt,visit, words ,answer):
    
    if now == target: # 탈출 분기점 
        if cnt < answer[0]:
            answer[0] = cnt
        return 
    
    for w in words:
        if connect_check(now , w)==True:
            if w not in visit:
                visit.append(w)
                dfs(w , target,cnt+1,visit,words , answer)
                visit.remove(w)



def solution(begin, target, words):

    # visit = {word:False for word in words}  # visit 을 꼭 True False로 할 필요 없움 
    answer = [10000]
    visit = []

    if target not in words: # 타겟이 리스트에 없으면 그냥 종료 
        return 0 
    
    dfs(begin,target,0,visit,words , answer)

    return answer[0]


print(solution("hit",	"cog"	,["hot", "dot", "dog", "lot", "log", "cog"]) )