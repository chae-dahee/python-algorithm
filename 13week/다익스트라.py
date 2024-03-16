import sys
sys.stdin = open('D_input.txt','r')

def getMin():
    min = INF
    wheremin = -1
    for now in range(V+1):
        if not Visited[now] and Distance[now] < min:
            min = Distance[now]
            wheremin = now
    return wheremin     #4

INF = int(1e5)
V, E = map(int,input().split())
MyMap = [[INF]*(V+1) for _ in range(V+1)]     #7*7, 빈칸 큰숫자넣음

for _ in range(E):  #입력받기
    start, stop, cost = map(int,input().split())
    MyMap[start][stop] = cost #edge개수만큼 돌림

Visited = [0]*(V+1)
Distance = [INF]*(V+1)
start = 0

Distance[start]=0

for i in range(V+1):
    if MyMap[i]: Distance[i] = MyMap[0][i]     #MyMap이 0이 아니면 그부분을 바꿔라! MyMap 한줄 distance에 불러오기

for i_ in range(V):     #단계별반복
    Shortest = getMin()     #최소정점찾기
    Visited[Shortest] = True

    for now in range(V+1):  #now=2 -> 9
        if Distance[now] > Distance[Shortest]+MyMap[Shortest][now]:
            Distance[now] = Distance[Shortest]+MyMap[Shortest][now]

    print(Distance)