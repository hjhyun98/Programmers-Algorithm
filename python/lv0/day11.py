# 주사위의 개수
def solution1(box, n):
    answer = 1
    for i in box:
       answer = answer * (i // n)
    return answer
    
# 합성수 찾기
def solution2(n):
    cnt = 0
    for num in range(1,n+1):
        i = 2
        while i < num:
            if num % i == 0:
                cnt += 1
                break
            i += 1
    return cnt

def solution2_2(n):
    result = 0
    for i in range(4, n +1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
    return output

# 최댓값 만들기 1
def solution3(numbers):
    numbers.sort(reverse=True)
    return numbers[0]*numbers[1]

def solution3_2(numbers):
    numbers.sort()
    return numbers[-1]*numbers[-2]

# 팩토리얼
def solution4(n):
    k = 1
    for i in range(1, 11):
        k = k * i
        if k == n:
            return i
        elif k > n:
            return i - 1
        