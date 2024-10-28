def solution(my_string, letter):
    answer = ''
    for char in my_string:
        if char != letter:  # letter가 아닌 경우
            answer += char
    return answer