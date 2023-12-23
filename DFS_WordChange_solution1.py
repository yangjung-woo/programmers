answer = 0
def solution(begin, target, words):

    dfs(begin, target, 0, words)
    return answer

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

def dfs(begin, target, d, words):
    global answer

    if begin == target:

        answer = d
        return
    else:
        if len(words) == 0:
            return 
        for w in range(len(words)):
            if connect_check(begin, words[w]):
                word = words[:w]+words[w+1:]
                dfs(words[w], target, d+1, word)

print(solution("hit",	"cog"	,["hot", "dot", "dog", "lot", "log", "cog"]) )