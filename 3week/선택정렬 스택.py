stack=[]

for now in range(1,6):  #스택에 1~5까지 값이 들어감
    stack.append(now)

#print(stack.pop())  #탑얘가 뽑힘
#print(stack.pop())
#print(stack.pop())
#print(stack.pop())
#print(stack.pop())
#print(stack)    #남아있는게 없음 다뽑힙

#스택의 top값 확인
print(stack[-1])

#거꾸로 출력
for _ in range(5):
    print(stack.pop(), end=' ')