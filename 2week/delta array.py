import sys
sys.stdin = open('input.txt', 'r')
Data = [list(map(int, input().split())) for i in range(5)]

dy = [-1,1,0,0] #상하
dx = [0,0,-1,1] #좌우
def isSafe(y,x):    #상하좌우가 0~4범위를 벗어나지 않도록
    if y >= 0 and y <= 4 and x >= 0 and x <= 4:
        return True
    else:
        return False

def myAbs(a,b): #절대값 구하는 식
    if a>b:
        return a-b
    else:
        return b-a

sum=0

for y in range (len(Data)): #5
    for x in range (len(Data)): #5
        for dir in range (len(dy)): #4 완탐
            newY = y + dy[dir]
            newX = x + dx[dir]
            if isSafe(newY,newX):
                sum+=myAbs(Data[y][x], Data[newY][newX])

print(sum)