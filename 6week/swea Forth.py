import sys
sys.stdin = open('Forth input.txt', 'r')

T = int(input())    #3
for tc in range(1,T+1):
    postFix = list(input().split())     #한줄 배열에 넣음
    stack = []    #숫자를 스택에 넣을것
    print("%d " %tc, end='')     #답찍을 형식 준비완

    for now in postFix: #하나씩 읽을것
        if now >= '0':  #숫자면, append 스택에 추가
            stack.append(int(now))  #정수 형변환
        elif now == '.':
            if len(stack) != 1:     #답이 나오지 않는 경우
                print('error')
            print(stack[0])     #수식끝, 마지막꺼 출력
        else:
            if now in ('+','-','*','/'):
                if len(stack) <2:
                    print('error')
                    break
                num2 = stack.pop()
                num1 = stack.pop()
                if now == '*':
                    temp = num1 * num2
                    stack.append(temp)
                elif now == '+':
                    temp = num1 + num2
                    stack.append(temp)
                elif now == '-':
                    temp = num1 - num2
                    stack.append(temp)
                elif now == '/':
                    temp = num1 // num2   #파이썬은 나누기기호 두번
                    stack.append(temp)