import sys
sys.stdin = open('swea_input.txt', 'r')

def isSafe(y,x):
    if 0<=x<16 and 0<=y<16 and Maze[y][x] != 1:
        return True
    else:
        return False
def DFS(y,x):
    global ans  #ans=0메인함수값을 받아옴, 바껴도 맨날받음
    if Maze[y][x] == 3:
        ans = 1
        return
    Maze[y][x] = 1      #visited 표시, 초반부터 바꾸면 도착지점3을 찾이 못함

    for dy, dx in (0,1), (0,-1), (-1,0), (1,0):     #delta 우좌상하
        newY = y + dy
        newX = x + dx
        if isSafe(newY, newX):
            DFS(newY, newX)

for tc in range(1,11):
    T = int(input())     #테스트케이스 수받기
    Maze = [list(map(int, input())) for _ in range(16)]
    ans = 0
    for y in range(16):
        for x in range(16):
            if Maze[y][x] == 2:     #start(1,1)찾음
                startX = y      #왜 startX인데 y값을 대입하지???
                startY = x

    DFS(startY, startX)     #완탐
    print(f"#{tc} {ans}")