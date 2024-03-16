import sys
sys.stdin = open('ladder input.txt', 'r')

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

    #isSafe없이 오, 왼에 길이 있나 탐색, 없으면 위로 -> 오,왼,위 -> eof만날때까지 / visitied 필요없음
    while True:
        if (x-1) >= 0 and MyMap[y][x-1] == 1:   #왼쪽 길이 있는가?
            while (x-1) >= 0 and MyMap[y][x-1] == 1:
                x-=1    #왼쪽으로
            y-=1
        elif (x+1) < 100 and MyMap[y][x+1] == 1:    #오른쪽 길이 있는가?
            while (x+1) < 100 and MyMap[y][x+1] == 1:
                x+=1    #오른쪽으로
            y-=1
        else:   #앞으로 가라
            y-=1
        if y==0:break
    print("#%d" %tc, x)