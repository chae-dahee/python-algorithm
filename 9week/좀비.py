import sys
sys.stdin = open('BFS_input.txt', 'r')

ability = [0]*3
Time=[987654321]*1000   #좀비위치가장큰수

Shalala, Zombie = map(int, input().split())
ability[0], ability[1], ability[2] = map(int, input().split())
Queue=[]
def BFS(here):
    while Queue:
        here = Queue.pop(0)
        for i in range(3):
            next = here + ability[i]
            if next > len(Time)-1:continue  #너무 길어지지 않도록
            if Time[next] > Time[here] + 1:      #distance 오래걸리는 큰것? -> 성능향상(완탐x 조건)
                Time[next] = Time[here] + 1
                Queue.append(next)
Time[Shalala]=0     #방문 초기화, 방문시 1로 바꾸기

if Shalala==Zombie: print(0)    #shalal == Zombie (0,0)이미 만남
else:
    Queue.append(Shalala)
    BFS(Shalala)

if Time[Zombie] != 987654321:print(Time[Zombie])    #찾음
else: print(-1)