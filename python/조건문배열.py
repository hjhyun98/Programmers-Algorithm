# 조건문1 - 숫자비교
def is_same(n1, n2):
    if n1 == n2:
        return 1
    else:
        return -1
    
# 분수의 덧셈 (day2)
def solution(numer1, denom1, numer2, denom2):
    answer = [(numer1*denom2)+(numer2*denom1),(denom1*denom2)]
    num = answer[1] - 1
    while num > 1:
        if answer[0] % num == 0 and answer[1] % num == 0:
            answer[0] = answer[0] / num
            answer[1] = answer[1] / num
        num -= 1
        
    return answer
    
# 배열 두배 만들기 (day2) - 반복문
def double_list(numbers):  
    answer = []
    for number in numbers:
        answer.append(number*2)
    return answer

