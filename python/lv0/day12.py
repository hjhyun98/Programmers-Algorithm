#  모음 제거
def solution1(my_string):
    answer = ''
    flag = True
    for ch in my_string:
        for i in ['a','e','i','o','u']:
            if ch == i:
                flag = False
        if flag == True:
            answer += ch
        flag = True
    return answer

def solution1_2(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
    return my_string

def solution1_3(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])

# 문자열 정렬하기 1
def solution2(my_string):
    numbers = []
    for i in my_string:
        if i in "0123456789":
            numbers.append(int(i))
    numbers.sort()
    return numbers

def solution2_1(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])

# 정규표현식 공부한 후 다시 보자
# import re

# def solution(my_string):
#     return sorted(map(int, (list(re.sub('[^0-9]', '', my_string)))))

# 숨어있는 숫자의 덧셈1

def solution3(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit():
            answer += int(i)
    return answer

def solution3_2(my_string):
    return sum(int(i) for i in my_string if i.isdigit())

def solution3_3(my_string):
    answer = 0 
    for i in my_string:
        try:
            answer += int(i)
        except:
            pass
    return answer

# 소인수분해
def solution4(n):
    answer = []
    for i in range(2, n+1):
        while True:
            if n % i == 0:
                if not(i in answer):
                    answer.append(i)
                n = n // i
            else: break
        if n == 1:
            break
    return answer

def solution4_2(n):
    answer= []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            if d not in answer:
                answer.append(d)
            else:
                d += 1
    return answer

