def solution(num_list):
    answer = []
    count_hol = 0
    count_jjak  = 0
    
    for num in num_list:
        if num % 2 == 0:
            count_hol += 1
        else:
            count_jjak += 1
    answer.append(count_hol)
    answer.append(count_jjak)
    return answer