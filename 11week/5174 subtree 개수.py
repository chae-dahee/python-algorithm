import sys
sys.stdin = open('5174_input.txt', 'r')

def preorder(here):
    global count
    if here:
        count=count+1
        preorder(Tree[here][0])     #LC
        preorder(Tree[here][1])     #RC

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())    #E=5, N=1
    Data = list(map(int, input().split()))
    Tree = [[0]*2 for _ in range(1002)]     #SWEA 패스1002?
    count = 0

    for i in range(E):
        parent, child = Data[2*i], Data[2*i+1]
        if Tree[parent][0] == 0:  # LC
            Tree[parent][0] = child
        else:
            Tree[parent][1] = child
    preorder(N)

    print(f'#{tc} {count}')