# 문자열 str이 주어집니다.
# 문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드를 작성해 보세요.
str = input()
list_str = list(str)
for i in range(len(list_str)):
    print(list_str[i])

# 더 쉬운 방법  
# print('\n'.join(input()))