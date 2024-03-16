import sys
sys.stdin = open('ladder input.txt', 'r')

dy = [0,0,-1]   #-1 상(위)으로 이동
dx = [-1,1,0]   # 좌, 우, 상

def isPossible(y,x):
    if 0 <= y < 100 and  0 <= x < 100 and (MyMap[y][x]==1):
        return True     #범위 안에 있으면 가도 된다
    else:
        return False

#도착하면 길을 지워줌
def GetSome(y,x):
    MyMap[y][x] = -1    #visitied대신
    if y == 0:  #제일 꼭대기에 위치함
        print("#%d" %tc, x)
        return

    for dir in range(3):
        newY = y+dy[dir]
        newX = x + dx[dir]
        if isPossible(newY, newX):  #이동해도 되는지 확인하는 함수
            GetSome(newY, newX)
            return      #이거 안쓰면 계속반복,, 완전탐색을 안하겠다는 뜻

for tc in range(1,11):
    input()     #문제번호 출력이 필요없으면, 그냥 읽기만 하겠다는 표시
    MyMap = [[0 for x in range(100)] for y in range(100)]

    for y in range(100):
        MyMap[y] = list(map(int, input().split()))      #입력받는 방법

    for x in range(100):
        if MyMap[99][x] == 2:   #처음출발지
            startX = x
    x = startX
    y = 99
    
    GetSome(y,x)    #계속방문!