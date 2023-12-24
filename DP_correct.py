# 올바른 괄호의 개수를 구해보시오 
# 이 문제는 카탈란 수 문제이다 
# https://m.blog.naver.com/pyw0564/221523147108 
# C0 =1   , Cn = sigma(i=1~ n-1)   Ci * Cn-1-i   for n>1
# 이 공식을 통해 DP로 구현


def solution(n):
    answer = 0
    dp = [0 for _ in range(n+1) ]
    dp[0] =1
    dp[1] =1

    for i in range(2,n+1):
        for j in range(1,i+1):
            dp[i] += dp[i-j] * dp[j-1]

    return dp[n]

print