def solution(array, height):
    count = 0  # 머쓱이보다 큰 사람의 수를 저장할 변수

    # 배열을 순회하면서 머쓱이보다 큰 키의 개수를 셉니다.
    for h in array:
        if h > height:
            count += 1  # 키가 머쓱이보다 큰 경우 count 증가

    return count  # 최종적으로 머쓱이보다 큰 사람 수 반환
