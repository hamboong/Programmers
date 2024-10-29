def solution(numbers, n):
    answer = 0
    for i in numbers:
        answer += i  # numbers의 요소를 answer에 더합니다.
        if answer > n:  # answer가 n을 초과하는 경우
            return answer  # answer를 반환
    return answer  # 모든 요소를 더한 후 반환 