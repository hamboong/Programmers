def solution(n, numlist):
    answer = []
    for num in numlist:
       if num % n == 0:  # n의 배수인 경우
           answer.append(num) 
    return answer