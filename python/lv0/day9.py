import math

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
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)

# 모스 부호
def solution2(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    answer = ''
    words = letter.split()
    for i in words:
        answer += morse[i]
    
    return answer

# 가위바위보
def solution3(rsp):
    answer = ''
    for i in rsp:
        if i == "0":
            answer += "5"
        elif i == "2":
            answer += "0"
        else:
            answer += "2"
    return answer

def solution3_2(rsp):
    d = {'0':'5', '2':'0', '5': '2'}
    return ''.join(d[i] for i in rsp)

def solution3_3(rsp):
    rsp = rsp.replace('2', 's')
    rsp = rsp.replace('5', 'p')
    rsp = rsp.replace('0', 'r')
    rsp = rsp.replace('r', '5')
    rsp = rsp.replace('s', '0')
    rsp = rsp.replace('p', '2')
    return rsp

# 구슬을 나누는 경우의 수
import math
def solution4(balls, share):
    answer = 1
    i = share+1
    while i <= balls:
        answer *= i
        i += 1
    return answer/math.factorial(balls-share)
    

def solution4_2(balls, share):
    answer = factorial(balls) / (factorial(balls- share)*factorial(share))
    
def factorial(n):
    result =1 
    for i in range(1, n+1):
        result = result * i
    return result

def solution4_3(balls, share):
    return math.comb(balls, share)

