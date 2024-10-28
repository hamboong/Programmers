def solution(money):
    answer = []
    coffee = money // 5500
    save_money = money % 5500
    answer.append(coffee)
    answer.append(save_money)
    return answer

