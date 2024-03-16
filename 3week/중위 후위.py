Data = "2+3*4/5"

stack = []
result = []

#기호와 숫자 다른 배열이 넣기
for i in range(len(Data)):
    if '*' <= Data[i] <= '/':
        stack.append(Data[i])
    elif '0' <= Data[i] <= '9':
        result.append(Data[i])

while stack:
    result.append(stack.pop())
print(''.join(result))