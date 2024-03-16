import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range (1, T+1):
    data = list(map(int, input().split()))

    max = -987654321
    wheremax = 0
    howmany = len(data)


    for now in range(howmany):
        if data[now] >max:
            max = data[now]
            wheremax = now

    print(f"#{tc}{max}")
    #print(f"이 중 최대값의 위치는 {wheremax + 1} 입니다.")
