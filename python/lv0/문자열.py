# 문자열 뒤집기
def solution(my_string):
    answer_list = list(my_string)
    answer_list.reverse()
    return ''.join(answer_list)

# 직각삼각형 출력하기
def print_right_triangle():
    n = int(input())
    for i in range(1, n+1):
        star = '*'*i
        print(star)
        
# 짝수 홀수 개수
def count_odd_even(num_list):
    answer = [0,0]
    for i in num_list:
        if i % 2== 0:
            answer[0] += 1
        else:
            answer[1] += 1
    return answer

# 문자 반복 출력하기
def print_string_ntimes(my_string, n):
    answer = ''
    for i in my_string:
        answer+=i*n
    return answer

# 특정 문자 제거하기
def ver1(my_string, letter):
    answer = ''
    for ch in my_string:
        if ch != letter:
            answer += ch
    return answer

def ver2(my_string, letter):
    return my_string.replace(letter, '')
