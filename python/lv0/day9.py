#  개미 군단
def solution1(hp):
    answer = 0
    while hp > 0:
        if hp >= 5:
            hp -= 5
        elif hp >= 3:
            hp -= 3
        else:
            hp -= 1
        answer += 1
    return answer

def solution1_2(hp):
    answer = hp // 5 
    hp %= 5 
    answer += hp // 3
    hp %= 3
    answer += hp // 1
    return answer

def solution1_3(hp):
    return hp // 5 + (hp % // 3) + ((hp % 5) % 3)