import sys
sys.stdin = open('J_input.txt', 'r')

goal, howmany = map(int, input().split())

MyMap = [[0]*(goal+1)for _ in range(goal+1)]    #8by8생성
visited = [0]*(goal+1)

for y in range(howmany):
    start, end, cost = map(int, input().split())
    MyMap[start][end] = cost
    MyMap[end][start] = cost

ans = 0

print(ans)