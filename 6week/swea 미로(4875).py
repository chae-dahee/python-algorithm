import sys
sys.stdin = open('미로 input.txt', 'r')

def DFS(y, x):
    global ans
    if Maze[y][x] == 3:
        ans = 1
        return
    Maze[y][x] = 1  # visited 표시

    for dy, dx in (0,1), (0,-1), (-1,0), (1,0):
        newY = y + dy
        newX = x + dx
        if isSafe(newY, newX):
            DFS(newY, newX)

def isSafe(y,x):
    if 0<=x<size and 0<=y<size and Maze[y][x] != 1:
        return True
    else:
        return False

T = int(input())
for tc in range(1, T+1):
    size = int(input())
    Maze = [list(map(int, input())) for _ in range(size)]
    ans = 0
    #시작지점 구하기
    for y in range(size):
        for x in range(size):
            if Maze[y][x] == 2:
                startX, startY = y, x
                break

    DFS(startY, startX)
    print(f"#{tc} {ans}")