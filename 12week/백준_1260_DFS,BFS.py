import sys
sys.stdin = open('1260_input.txt', 'r')

V, E, start = map(int,input().split())

MyMap = [[] for _ in range(V+1)]

for _ in range(E):
    _from, _to = map(int,input().split())    #_from = 1, _to = 2
    MyMap[_from].append(_to)    #표에 저장하는 과정
    MyMap[_to].append(_from)    #양방향이기 때문에 반대도 실행

for now in MyMap:   #입력값 정렬
    now.sort()

def DFS(here):
    print(here,end=' ')
    Visited[here] = True
    for next in MyMap[here]:
        if not Visited[next]:   #방문한 적이 없다면?
            DFS(next)

def BFS(here):
    Queue = []
    Queue.append(here)
    Visited[here] = True

    while Queue:
        here = Queue.pop(0)
        print(here, end=' ')
        for next in MyMap[here]:
            if not Visited[next]:
                Queue.append(next)
                Visited[next] = True

Visited = [False] * (V+1)
DFS(start)
print()
Visited = [False] * (V+1)
BFS(start)