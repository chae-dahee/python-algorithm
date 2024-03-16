import sys
sys.stdin = open('input.txt', 'r')

howmany = int(input())  #howmany = 3

for tc in range (1, howmany+1):  #3번 실행
    Data = list(map(int, input().split()))
    Count = [0] * 10

    #Count sort
    for i in range(len(Data)):
        Count[Data[i]]+=1

    run, triplet = 0,0

    #triplet
    for i in range(len(Count)):
        if Count[i] >= 3:
            triplet += 1
            Count[i] -= 3  #사용한 카드 빼기

    #run
    for i in range(len(Count)-2):
        if Count[i] >= 1 and Count[i+1] >= 1 and Count[i+2] >= 1:
            run += 1
            #123인식이 안되는 이유가 사용한 카드 안빼서/...?

    if run+triplet == 2:
        print(f"#{tc} Win")
    else:
        print(f"#{tc} LOSE")