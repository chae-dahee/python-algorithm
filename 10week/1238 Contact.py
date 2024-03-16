import sys
sys.stdin = open('1238.txt', 'r')
#마지막에 연락받은 사람 중 제일 큰 숫자

def BFS(here):
    Queue=[start]
    Visited[start]=0

    while Queue:
        here = Queue.pop(0)
        for next in Mymap[here]:    #방문표시
            if Visited[next] == 0:
                Visited[next] = Visited[here]+1
                Queue.append(next)


for tc in range(1,11):
    Visited = [0]*101
    howmany, start = map(int, input().split())    #길이, 시작점
    Data = list(map(int, input(). split()))
    Mymap = [[] for _ in range(101)]

    for i in range(0, len(Data), 2):   #from, to 구분해서 Mymap에 저장
        f, t = Data[i], Data[i+1]
        Mymap[f].append(t)

    BFS(start)

    max = -1
    for i in range(len(Visited)):   #같은도착시간 최대값
        if Visited[i] >= max:
            max = Visited[i]
            ans = i

    print(f'#{tc} {ans}')