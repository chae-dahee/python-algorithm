import sys
sys.stdin = open('DFS-input.txt', 'r')

graph =[[0 for _ in range(2)] for __ in range(8)]
stack=[]
visited=[here] = True
ans=[]

visited, stack = list(), list()

while True:
    MyMap = list(map(int, input().split()))

def DFS(here):
    stack.append(here)
        if next:
            stack.append(here)
        while next:
            here = next
            next = findnext(here)
            if next:
                visitied.append(here)
        here = visitied.pop()

    print(here)
    visitied = list()