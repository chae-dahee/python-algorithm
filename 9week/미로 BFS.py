import sys
sys.stdin = open('미로BFS_input.txt', 'r')

row, col = map(int,input().split())
MyMap=[]
Queue=[]

Visited = [[0]*col for _ in range(row)]    #map과 같은! 2차원 배열이어야함 [0]값으로 채워진 5*5

def isPossible(y,x):
    if 0<=y<5 and 0<=x<5 and MyMap[y][x] != '#' and not Visited[y][x]:
        return True
    else:
        return False

#상하좌우
dy=[-1,1,0,0]
dx=[0,0,-1,1]

for _ in range(row):
    MyMap.append(input())
###맵넣었음

for y in range(5):
    for x in range(5):
        if MyMap[y][x] == 'S':  #시작점
            statY = y
            statX = x
            Queue.append([statY,statX])     #x,y,값 둘다 저장! 리스트 활용
            Visited[statY][statX] = True   #방문표시

while Queue:
    y, x = Queue.pop(0)     #큐에 있는 y,x 리스트 값을 각 변수에 한번에 pop으로 넣음
    if MyMap[y][x] == 'G':
        print('Arrived')
    for dir in range(4):    #상하좌우에 길이 있으면 큐에 appned
        newY = y+dy[dir]
        newX = x+dx[dir]
        if isPossible(newY, newX):
            Visited[newY][newX] = True
            Queue.append([newY, newX])