def solution(myString):
    answer = ''
    for i in myString:
        if i == 'a':
            answer += 'A'
        elif 'B'<=i<='Z':
            answer += i.lower()
        else:
            answer += i
    return answer
