def solution(arr):
    answer = []
    last = -1

    for i in arr:
        if i != last:
            answer.append(i)
            last = i

    return answer