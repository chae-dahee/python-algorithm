import sys
sys.stdin = open('5105.txt', 'r')

#밖에 나갈 경우
def isSafe(y,x):
    if 0<=x<size and 0<=y<size and Maze[y][x] != 1:
        return True
    else:
        return False

def BFS(y, x):
    Queue = [(y,x)]
    Distance = [[0] * size for _ in range(size)]
    print(Queue)

    while Queue:
        y, x = Queue.pop(0)     #큐에 있는 y,x 리스트 값을 각 변수에 한번에 pop으로 넣음
        if Maze[y][x] != 3:     #방문처리
            Maze[y][x] = 1

        for dy, dx in (0,1), (0,-1), (-1,0), (1,0):
            newY = y + dy
            newX = x + dx
            if isSafe(newY, newX):
                if Maze[newY][newX] == 0:   #거리측정
                    Distance[newY][newX] = Distance[y][x] + 1
                    Queue.append([newY,newX])
                elif Maze[newY][newX] == 3:     #결과
                    return Distance[y][x]
    return 0


T = int(input())
for tc in range(1, T+1):
    size = int(input())
    Maze = [list(map(int,input())) for _ in range(size)]
    ans = 0

    #시작점 찾기
    for y in range(size):
        for x in range(size):
            if Maze[y][x] == 2:
                startX, startY = x, y

    print(f'#{tc} {BFS(startY, startX)}')
