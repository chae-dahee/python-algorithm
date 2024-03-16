import sys
sys.stdin = open('01_input.txt','r')

def BFS(num,k):
    Queue = []
    for i in range(num):
        for r in range(1,num):
            if Data[i] > Data[r]:
                if Data[i]-Data[r] < k:
                    Queue.append(Data[i])
                    Queue.append(Data[r])
                else:
                    continue
            elif Data[r] > Data[i]:
                if Data[r]-Data[i] < k:
                    Queue.append(Data[i])
                    Queue.append(Data[r])
                else:
                    continue

            elif len(Queue) == 0:
                Queue.append(0)
                Queue.append(0)

    return int(len(Queue)/2)

T = int(input())
for x in range(1,T+1):
    N, K = map(int,input().split())
    Data = list(map(int,input().split()))

    print(f'#{x} {BFS(N,K)}')

#1 3
#2 4
#3 1