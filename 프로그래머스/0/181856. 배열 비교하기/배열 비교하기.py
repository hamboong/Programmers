def solution(arr1, arr2):
    answer = 0
    value1 = sum(arr1)  # arr1의 모든 요소의 합
    value2 = sum(arr2)  # arr2의 모든 요소의 합

    # 배열의 길이 비교
    if len(arr1) > len(arr2):
        answer = 1
    elif len(arr1) < len(arr2):
        answer = -1
    else:
        # 길이가 같을 경우 합계를 비교
        if value1 > value2:
            answer = 1
        elif value1 < value2:
            answer = -1
        else:
            answer = 0
    return answer
