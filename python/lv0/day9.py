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