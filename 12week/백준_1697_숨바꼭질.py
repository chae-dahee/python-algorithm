import sys
sys.stdin = open('1697_input.txt', 'r')

N, K = map(int,input().split())
MAX = 100000
Visited = [0] * (MAX + 1)

#순간이동 2N
#이동 N+1
def BFS():
    Queue = []
    Queue.append(N)

    while Queue:
        x = Queue.pop()
        if x == K:
            print(Visited[x])
            break
        for next in (x-1, x+1, x*2):
            if 0 <= next <= MAX and not Visited[next]:
                Visited[next] = Visited[x] + 1
                Queue.append(next)

BFS()
