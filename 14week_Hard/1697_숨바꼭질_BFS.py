import sys
sys.stdin = open('1697_input.txt', 'r')

n, k = map(int,input().split())
MAX = 100000
Visited = [0]*(MAX+1)

def BFS():
    Queue = []
    Queue.append(n)

    while Queue:
        x = Queue.pop(0)
        if x == k:
            print(Visited[x])
            break
        for next in (x-1, x+1, x*2):
            if 0 <= next <= MAX and not Visited[next]:
                Visited[next] = Visited[x]+1
                Queue.append(next)

BFS()