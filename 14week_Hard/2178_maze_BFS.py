import sys
sys.stdin = open('2178_input.txt', 'r')

n, m = map(int,input().split())
Maze = [list(map(int,input())) for _ in range(n)]

#상하좌우
dy=[-1,1,0,0]
dx=[0,0,-1,1]

def isSafe(y,x):
    if 0<=y<n and 0<=x<m:
        return True
    else:
        return False

def BFS(y, x):
    Queue = []
    Queue.append((x,y))

    while Queue:
        y, x = Queue.pop(0)  # 큐에 있는 y,x 리스트 값을 각 변수에 한번에 pop으로 넣음

        for dir in range(4):  # 상하좌우에 길이 있으면 큐에 appned
            newY = y + dy[dir]
            newX = x + dx[dir]

            if isSafe(newY, newX):
                if Maze[newY][newX] == 1:
                    Maze[newY][newX] = Maze[y][x] + 1
                    Queue.append((newY, newX))

BFS(0,0)
print(Maze[n-1][m-1])