# 배열 자르기
def solution1(numbers, num1, num2):
    return numbers[num1:num2+1]

# 외계 행성의 나이
def solution2(age):
    print(age)
    alpha = ['a','b','c','d','e','f','g','h','i','j']
    answer = []
    while age > 0:
        print(age)
        answer.append(alpha[age%10])
        print(answer)
        age //= 10
    answer.reverse()
    return ''.join(answer)

def othersolution2(age):
    return ''.join([chr(int(i)+97) for i in str(age)])

# 진료순서 정하기
def solution3(emergency):
    answer = [0 for i in range(len(emergency))]
    for i in range(len(emergency)):
        idx = emergency.index(max(emergency))
        answer[idx] = i+1
        emergency[idx] = 0     
    return answer

def othersolution3(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]

# 순서쌍의 개수
def solution4(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += 1
    return answer


import sys 
read = sys.stdin.readline
data = list(map(int,read().split()))
print(solution3(data))