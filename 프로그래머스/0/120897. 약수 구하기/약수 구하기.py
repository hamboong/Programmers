def solution(n):
    answer = []  # 약수를 저장할 리스트 초기화
    for i in range(1, n + 1):  # 1부터 n까지 반복
        if n % i == 0:  # n이 i로 나누어 떨어지는지 확인
            answer.append(i)  # 약수라면 리스트에 추가
    return answer  # 모든 약수를 반환
