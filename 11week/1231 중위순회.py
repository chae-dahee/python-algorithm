import sys
sys.stdin = open('1231_input.txt', 'r')

def inorder(here):  # 1
    if here:
        inorder(Tree[here][0])  # LC
        print('%d ' %here, end='')  # root
        inorder(Tree[here][1])  # RC


for tc in range(1,11):
    N = int(input())    #8
    Tree = [[0]*2 for _ in range(N)]    #1 W 2 3

    for i in range(N):
        Data = list(input().split())
        if len(Data) == 2:
            Data.append('0')
            Data.append('0')
        elif len(Data) == 3:
            Data.append('0')
        print(Data)

        parent, child = Data[2 * i], Data[2 * i + 1]
        if Tree[int(parent)][0] == 0:  # LC
            Tree[int(parent)][0] = child
        else:
            Tree[int(parent)][1] = child
    inorder(N)
