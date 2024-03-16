import sys
sys.stdin = open('미로 input.txt', 'r') # 파일에서 읽을 때
def isSafe(y, x):
    if  0 <= x < 16 and 0 <= y < 16 and Maze[y][x] != 1 :
        return True
    else :
        return False
def DFS(y, x):
    global ans
    if Maze[y][x] == 3 :
        ans = 1
        return
    Maze[y][x] = 1
    for dy, dx in (0, 1), (0, -1), (-1, 0), (1, 0):	#우좌상하 순으로 탐색
        newY= y+dy
        newX = x + dx
        if isSafe(newY, newX) :
            DFS(newY, newX)

for tc in range(1, 11):
    T = int(input())
    Maze=[list(map(int,input())) for _ in range(16)]
    ans = 0
    for y in range(16):
        for x in range(16):
            if Maze[y][x] == 2 :
                startX = x
                startY = y

    DFS(startY, startX)
    print(f"#{tc} {ans}")
