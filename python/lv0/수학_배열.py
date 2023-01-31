# 피자 나눠먹기1  
def pizza1(n):
    if n % 7 == 0:
        return n/7
    else:
        return n // 7 + 1
    
# 피자 나눠먹기 2 
def pizza2(n):
    answer = 6
    while answer % n != 0:
        answer += 6
    return answer/6

# 피자 나눠먹기 3
def pizza3(slice, n):
    answer = 1
    while (slice*answer) < n:
        answer += 1
    return answer

# 배열의 평균값
def get_average(numbers):
    answer = sum(numbers)
    return answer/len(numbers)

# 옷가게 할인받기
import math 

def discount(price):
    if price >= 500000:
        return math.trunc(price*0.8) 
    elif price >= 300000:
        return math.trunc(price*0.9) 
    elif price >= 100000:
        return math.trunc(price*0.95) 
    else:
        return price
  
#   아이스 아메리카노
def ice_americano(money):
    answer = [(money // 5500)]
    answer.append(money - (answer[0]*5500))
    return answer

# 나이 출력
def get_year(age):
    return 2023-age + 1
    
# 배열 뒤집기
def reverse_list(num_list):
    num_list.reverse()
    return num_list
   