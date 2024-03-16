import sys
sys.stdin = open('28278_input.txt', 'r')

#명령의 수
N = int(input())

#정수 저장하는 스택
Stack = []

def Order(o):
    if o == 2:
        if len(Stack) == 0:
            print(-1)
        else:
            print(Stack.pop(-1))    #Stack.pop(len(Stack)-1)

    elif o == 3:
        print(len(Stack))

    elif o == 4:
        if len(Stack) == 0:
            print(1)
        else:
            print(0)

    elif o == 5:
        if len(Stack) != 0:
            print(Stack[-1])
        else:
            print(-1)

for i in range(N):
    arr = list(map(int,input().split()))

    if arr[0] == 1:
        Stack.append(arr[1])
    else:
        Order(arr[0])