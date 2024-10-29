def solution(arr, n):
    answer = []
    if len(arr) % 2 == 1:  # 길이가 홀수인 경우
        for i in range(len(arr)):
            if i % 2 == 0:  # 짝수 인덱스일 때
                answer.append(arr[i] + n)
            else:
                answer.append(arr[i])
    else:  # 길이가 짝수인 경우
        for i in range(len(arr)):
            if i % 2 == 1:  # 홀수 인덱스일 때
                answer.append(arr[i] + n)
            else:
                answer.append(arr[i])
    return answer
