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

# 중앙값 구하기
def get_mid_val(array):
    array.sort()
    if len(array) % 2 == 0:
        return array[len(array)//2-1]
    else:
        return array[len(array)//2]
    
    
# 최빈값 구하기
def get_mode(array):
    max_count = -1 
    n = 0
    flag = False
    while n < 1000:
        if array.count(n) > max_count:
            max_count = array.count(n)
            max_num = n
            flag = False
        elif array.count(n) == max_count:
            flag = True
        n+=1
    if flag == True:
        return -1
    else:
        return max_num
    
# 짝수는 싫어요
def only_odd(n):
    answer = []
    m = 1
    while m <= n:
        answer.append(m)
        m += 2
            
    return answer

# 각도기
def angle(angle):
    if angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif angle <180:
        return 3
    else:
        return 4
    
# 양꼬치
def lamb_skewers(n, k):
    return n * 12000 + (k - n // 10) * 2000