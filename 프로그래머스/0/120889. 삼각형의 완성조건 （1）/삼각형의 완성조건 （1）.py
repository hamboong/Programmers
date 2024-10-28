import statistics

def solution(sides):
    if max(sides) < min(sides) + statistics.median(sides):
        answer = 1
    else:
        answer = 2
    return answer