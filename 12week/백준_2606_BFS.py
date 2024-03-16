import sys
sys.stdin = open('2606_input.txt', 'r')

V = int(input())
E = int(input())
ans = 0

MyMap = [[] for _ in range(V+1)]

for _ in range(E):
    _from, _to = map(int,input().split())
    MyMap[_from].append(_to)
    MyMap[_to].append(_from)

for now in MyMap:   #입력값 정렬
    now.sort()

def BFS(here):
    Queue = [here]
    Visited[here] = True
    global ans

    while Queue:
        here = Queue.pop(0)
        for next in MyMap[here]:
            if not Visited[next]:
                Queue.append(next)
                Visited[next] = True
                ans += 1

Visited = [False]*(V+1)
BFS(1)
print(ans)