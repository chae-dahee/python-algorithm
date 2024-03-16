import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range (1, T+1):
    Data = list(map(int, input().split()))

    max = -987654321
    min = 987654321
    wheremax = 0
    wheremin = 0
    temp = [0]*10

    for now in range(len(Data)):
        if Data[now] > max:
            max = data[now]
            wheremax = now

    for i in range(len(Data)):
        if Data(i) < min:
            min = data[i]
            wheremin = i


    print(f"#{tc}{max}")
    print(f"이 중 최대값의 위치는 {wheremax + 1} 입니다.")

