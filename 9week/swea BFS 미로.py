import sys
sys.stdin = open('swea BFS 미로_input.txt', 'r')

def isPossible(y, x):
    if 0 <= y < size and 0 <= x < size and MyMap[y][x] != 1:
        return True
    else:
        return False

T=int(input())
for tc in range(1,T+1):
    size = int(input())
    MyMap=[list(map(int, input())) for _ in range(size)]
    Queue=[]
    Visited = [[0]*size for _ in range(size)]    #map과 같은! 2차원 배열이어야함 [0]값으로 채워진 5*5
    ans=0

    print(MyMap)

    #상하좌우
    dy=[-1,1,0,0]
    dx=[0,0,-1,1]

    for y in range(size):
        for x in range(size):
            if MyMap[y][x] == 2:
                startX, startY = y, x
                Queue.append([startX, startY])  # x,y,값 둘다 저장! 리스트 활용
                Visited[startY][startX] = True  # 방문표시

    while Queue:
        y, x = Queue.pop(0)     #큐에 있는 y,x 리스트 값을 각 변수에 한번에 pop으로 넣음
        if MyMap[y][x] == 3:
            ans = 1
        for dir in range(4):    #상하좌우에 길이 있으면 큐에 appned
            newY = y+dy[dir]
            newX = x+dx[dir]
            if isPossible(newY, newX) and Visited[newY][newX] == 0:
                Visited[newY][newX] = True
                Queue.append([newY, newX])


    print(f'#{tc} {ans}')