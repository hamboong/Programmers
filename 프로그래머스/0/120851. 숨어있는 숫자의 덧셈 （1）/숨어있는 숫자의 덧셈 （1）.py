def solution(my_string):
    answer = 0  # 합계를 저장할 변수

    for char in my_string:  
        if char.isdigit():  # 문자가 숫자인 경우
            answer += int(char)  # 숫자로 변환하여 합산

    return answer  # 최종 합계 반환