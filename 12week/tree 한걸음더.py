import sys
sys.stdin = open('tree_input.txt', 'r')

V, E = map(int,input().split())

Tree = [[0]*5 for _ in range(V+1)]

for i in range(V+1):    #부모, 레벨은 -1로 초기화
    Tree[i][3] = Tree[i][4] = -1

Tree[1][4] = 0  #1의 레벨 0으로 초기화
Data = list(map(int,input().split()))

for i in range(E):
    p, c = Data[i*2], Data[i*2+1]

    if Tree[p][0] == 0:
        Tree[p][0] = c
        Tree[p][2] += 1
        Tree[c][3] = p
        Tree[c][4] = Tree[p][4] + 1    #부모레벨+1=자식레벨
    else:
        Tree[p][1] = c
        Tree[p][2] += 1
        Tree[c][3] = p
        Tree[c][4] = Tree[p][4] + 1

#레벨 별 출력

for level in range(5):
    for n in range(V+1):
        if Tree[n][4]  == level:
            print(n, end=' ')
    print()

# for n in range(V+1):
#     if Tree[n][4] == 0:
#         print(n)
#     elif Tree[n][4] == 1:
#         print(n, end=' ')
#     print()
#     elif Tree[n][4] == 2:
#         print(n, end=' ')
#     elif Tree[n][4] == 3:
#         print(n, end=' ')
#     elif Tree[n][4] == 4:
#         print(n, end=' ')
#     elif Tree[n][4] == 5:
#         print(n, end=' ')