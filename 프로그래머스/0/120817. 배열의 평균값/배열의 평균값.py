def solution(numbers):
    sum = 0
    for num in numbers: # numbers[i]가 아니라 numbers 임
        sum += num
    answer = sum / len(numbers)  # len(numbers)
    return answer
