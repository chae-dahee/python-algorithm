import sys
sys.stdin = open('BFS_input.txt', 'r')
MyMap=[[0 for _ in range(8)] for __ in range(8)]
Visited = [0]*8    #방문했는지 아닌지 넣어주는 리스트(대문자로시작)
Queue=[]
Distance = [0]*8
Parent = [0]*8

V, E = map(int, input().split())    #E:8    v:7

for _ in range(E):
    start, stop = map(int, input().split())
    MyMap[start][stop]=1
    MyMap[stop][start]=1

start = 1
Queue.append(start)
Distance[start] = 0
Parent[start] = 0

while Queue:
    here = Queue.pop(0)
    print(here)
    Visited[here]=True

    for next in range(8):
        if MyMap[here][next] and not Visited[next] and next not in Queue:   #Map에 다음이 있고, visitied에 없으면, 큐에도 없고
            Queue.append(next)     #관련값 모두 큐에 넣어라
            #추가
            Distance[next] = Distance[here]+1
            Parent[next] = here


    print(Distance)
