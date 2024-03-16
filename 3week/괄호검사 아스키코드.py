import sys
sys.stdin = open('../3week/input.txt', 'r')

stack = []
Info = [0] * 128    #아스키코드 7비트라 [')'] = '(' ['}'] = '{' ['>'] = '<' [']'] = '[' 딕셔너리와 유사개념
#ord 함수로 아스키코드 사용선언, 오류처리!
Info[ord(')')] = '('
Info[ord('}')] = '{'
Info[ord('>')] = '<'
Info[ord(']')] = '['

Data = input()

for i in range(len(Data)):
    if Data[i] in '{[(<':
        stack.append(Data[i])
    elif stack[-1]==Info[ord(Data[i])]:  #4가지를 모두 쓰지 않아도됨!!! SWEA 문제에도 적용가능
        stack.pop()

print(Info)