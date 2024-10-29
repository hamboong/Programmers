def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if i % 2 == 1:  # 인덱스가 홀수일 경우
            answer.append(strArr[i].upper())  # 대문자로 추가
        else:  # 인덱스가 짝수일 경우
            answer.append(strArr[i].lower())  # 소문자로 추가
    return answer