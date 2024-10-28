def solution(array):
    array.sort()  #.sort()
    middle_index = len(array) // 2  # 중앙 인덱스 계산
    return array[middle_index]  # 중앙값 반환
