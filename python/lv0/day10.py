# 점의 위치 구하기
def solution1(dot):
    if dot[0] > 0 and dot[1] > 0:
        return 1
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    elif dot[0] < 0 and dot[1] < 0:
        return 3
    else:
        return 4

def solution1_2(dot):
    x,y = dot
    if x*y > 0:
        return 1 if x > 0 else 3
    else:
        return 4 if x > 0 else 2
    
# 2차원으로 만들기
def solution2(num_list, n):
    answer = []
    i = 0
    while i < len(num_list):
        if (i+1) % n == 0:
            answer.append(num_list[i-n+1:i+1])
        i += 1
    return answer

def solution2_2(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer

# 공 던지기
def solution3(numbers, k):
    answer = 1
    for i in range(1,k):
        answer += 2
        if answer > len(numbers):
            answer = answer - len(numbers)
    return answer

def solution3_2(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]

# 배열 회전시키기
def solution4(numbers, direction):
    if direction == "right":
        numbers.insert(0,numbers.pop())
    else:
        temp = numbers[0]
        del numbers[0]
        numbers.append(temp)
    return numbers

def solution4_2(numbers, direction):
    return [numbers[-1] + numbers[:-1] if direction == 'right' else numbers[1:] + numbers[0]]
