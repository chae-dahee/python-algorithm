import sys
sys.stdin = open('../3week/input.txt', 'r')

stack=[]
Data = input()
ans=0

for i in range(len(Data)):
    if Data[i] in '({': #C에선 일케.. Data[i]=='(' or Data[i]=='{'
        stack.append(Data[i])
    elif stack and ((Data[i]==')' and stack[-1]=='(') or (Data[i]=='}' and stack[-1]=='{') or (Data[i]==']' and stack[-1]=='[') or (Data[i]=='>' and stack[-1]=='<')): #안될경우? and 논리연산자의 오류
        stack.pop()
    else:break

if not stack : ans = 1  #스택이 비어있다 -> ans 1,
print(ans)