def solution(n):
    # 정수를 문자열로 변환하고, 각 문자를 정수로 변환하여 합산
    digit_sum = sum(int(digit) for digit in str(n))
    return digit_sum