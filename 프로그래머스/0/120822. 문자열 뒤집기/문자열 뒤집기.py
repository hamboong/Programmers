def solution(my_string):
    answer=list(my_string)
    box=""
    for i in range(len(answer)-1,-1, -1):
        box+=answer[i]
    return box
