def solution(angle):
    if 0 < angle < 90 :
        value = 1
    elif angle == 90: 
        value =  2
    elif 90<angle<180:
        value =  3
    elif angle ==180:
        value =  4
    return value
