def solution(arr):
    answer = []
    for i in arr:
        if (i < 50) and (i % 2 == 1):  # 홀수이고 50보다 작은 경우
            answer.append(i * 2)       # 두 배로 추가
        elif (i >= 50) and (i % 2 == 0):  # 짝수이고 50 이상인 경우
            answer.append(i // 2)      # 정수 나누기 추가
        else:
            answer.append(i)            # 조건에 맞지 않는 경우 원래 값 추가
    return answer
