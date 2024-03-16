import sys
sys.stdin = open('swea_input.txt', 'r')

for tc in range(1, 11):
    t, e = map(int, input().split())
    MyMap = {i: [] for i in range(100)}
    Edge = list(map(int, input().split()))
    Visited = {i: False for i in range(100)}

    for i in range(0, len(Edge), 2):
        MyMap[Edge[i]] += [Edge[i + 1]]

    Visited[0] = True


    def DFS(here):
        if here == 99:
            return True

        for next in MyMap[here]:
            if not Visited[next]:
                Visited[i] = True
                if DFS(next):
                    return True


    if DFS(0):
        print(f"#{t} 1")
    else:
        print(F"#{t} 0")