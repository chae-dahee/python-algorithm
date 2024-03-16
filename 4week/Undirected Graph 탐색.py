import sys
sys.stdin = open('input.txt', 'r')
MyMap=[[0 for _ in range(8)] for __ in range(8)]

Visited = [0]*8     #방문했는지 아닌지 넣어주는 리스트(대문자로시작)

V, E = map(int, input().split())    #E:8    v:7

for _ in range(E):
    start, stop = map(int, input().split())
    MyMap[start][stop]=1
    MyMap[stop][start]=1    #양방향이기 때문에 두번!

def DFS(here):
    print(here)
    Visited[here]=True

    for next in range(V+1):
        if MyMap[here][next] and not Visited[next]:
            DFS(next)

DFS(3)