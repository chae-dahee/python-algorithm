import sys
sys.stdin = open('input.txt', 'r')

def DFS(here):
    visited[here]=1
    for next in range(100):
        if MyMap[here][next] and not visited[next]:
            DFS(next)

for num in range(1,11):
    MyMap = [[0 for _ in range(100)] for _ in range(100)]
    tc, howmany = map(int,input().split())
    Data = list(map(int, input().split()))

    visited = [0] * 100

    for i in range(howmany):
        start, stop = Data[i*2], Data[i*2+1]
        MyMap[start][stop] = 1

    DFS(0)
    print(f"#{tc}, {visited[99]}")