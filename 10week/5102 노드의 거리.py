import sys
sys.stdin = open('5102.txt', 'r')

def BFS(S, G):
    Queue.append(S)     #시작점 설정
    Visited[S] = 1      #방문

    while Queue:
        stop = Queue.pop(0)
        for i in MyMap[stop]:
            if not Visited[i]:      #방문하지 않았다면
                Visited[i] = 1      #방문처리
                Distance[i] = Distance[stop]+1      #거리
                Queue.append(i)

                if i == G:  #도착하면
                    return Distance[i]
    return 0

T=int(input())
for tc in range(1,T+1):

    V, E = map(int, input().split())    #6 5, 7 4, 9 9

    MyMap = [[] for _ in range(V+1)]    #[[], [4, 3], [3, 5], [1, 2], [1, 6], [2], [4]]

    for _ in range(E):
        start, stop = map(int, input().split())
        MyMap[start].append(stop)
        MyMap[stop].append(start)

    S, G = map(int, input().split())    #1 6, 1 5, 1 9

    Visited = [0] * (V+1)
    Distance = [0] * (V+1)
    Queue = []

    print(f'#{tc} {BFS(S, G)}')