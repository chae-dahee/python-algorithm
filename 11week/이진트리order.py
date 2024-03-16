import sys
sys.stdin = open('tree_input.txt', 'r')

V, E = map(int, input().split())
Data = list(map(int, input().split()))
Tree = [[0]*2 for _ in range(V+1)]  #LC, RC 비어있는 트리배열 만듬

def preorder(here): #1
    if here:
        print('%d ' %here, end='')    #root
        preorder(Tree[here][0])     #LC
        preorder(Tree[here][1])     #RC


def inorder(here):  # 1
    if here:
        inorder(Tree[here][0])  # LC
        print('%d ' %here, end='')  # root
        inorder(Tree[here][1])  # RC


def postorder(here):  # 1
    if here:
        postorder(Tree[here][0])  # LC
        postorder(Tree[here][1])  # RC
        print('%d ' %here, end='')  # root


for i in range(E):
    parent, child = Data[2*i], Data[2*i+1]  #parnet = 1, child = 2
    if Tree[parent][0] == 0:     #LC
        Tree[parent][0] = child
    else:
        Tree[parent][1] = child

preorder(1)
print('\n')
inorder(1)
print('\n')
postorder(1)