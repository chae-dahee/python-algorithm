import sys
sys.stdin = open('tree_input.txt', 'r')

V, E = map(int, input().split())
Data = list(map(int, input().split()))

Tree = [[0]*2 for _ in range(V+1)]  #LC, RC 비어있는 트리배열 만듬

for i in range(E):
    parent, child = Data[2*i], Data[2*i+1]  #parnet = 1, child = 2
    if Tree[parent][0] == 0:     #LC
        Tree[parent][0] = child
    else:
        Tree[parent][1] = child

print(Tree)
