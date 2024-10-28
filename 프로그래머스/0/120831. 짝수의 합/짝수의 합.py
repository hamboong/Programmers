def solution(n):
    num = n//2
    answer = 0
    for i in range(1, n + 1):
        if i % 2 == 0:  # 짝수인 경우
            answer += i
    return answer