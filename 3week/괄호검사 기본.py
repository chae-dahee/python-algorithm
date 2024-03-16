import sys
sys.stdin = open('../3week/input.txt', 'r')

stack=[]
Data = input()
ans=0

for i in range(len(Data)):
    if Data[i] in '({': #C에선 일케.. Data[i]=='(' or Data[i]=='{'
        stack.append(Data[i])
    elif stack and ((Data[i]==')' and stack[-1]=='(') or (Data[i]=='}' and stack[-1]=='{')):
        stack.pop()
    else:break

if not stack : ans = 1
print(ans)