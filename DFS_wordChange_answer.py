def cmp(a,b):
	s1 = list(a)
	s2 = list(b)
	df = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			df += 1 
	if df == 1:
		return True
	else:
		return False

def solution(begin, target, words):
	answer = [100000]
	visit = [begin]
	if target not in words:
		return 0
	dfs(target, words, 0, visit, answer, begin)
	return answer[0]
	
def dfs(target, words, c, visit, answer, current):
	if target == current:
		if c < answer[0]:
			answer[0] = c
		return
	for i in range(len(words)):
		if cmp(words[i], current):
			if words[i] not in visit:				
				visit.append(words[i])
				dfs(target, words, c+1, visit, answer, words[i])
				visit.remove(words[i])
				
print(solution("hit",	"cog"	,["hot", "dot", "dog", "lot", "log", "cog"]))