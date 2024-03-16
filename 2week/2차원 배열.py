import sys
sys.stdin = open('input.txt', 'r')
Data = [list(map(int, input().split())) for i in range(9)]

max = Data[0][0]
whereY, whereX = -1,-1  #y,x 위치값

for y in range(len(Data)):
    for x in range(9):  #len(Data) = 9 같은거임~~~
        if Data[y][x] > max:
            max = Data[y][x]
            whereY = y
            whereX = x

print(max)
print(whereY+1,whereX+1)