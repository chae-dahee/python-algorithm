import sys
sys.stdin = open('11866_input.txt', 'r')

n, k = map(int,input().split())
Queue = []
Dead = []

for p in range(1,n+1):
    Queue.append(p)
print('<', end='')
while len(Queue) != 0:

    for _ in range(k-1):
        live = Queue.pop(0)
        Queue.append(live)
    tx = Queue.pop(0)
    Dead.append(tx)

Dead_str = str(Dead)[1:-1]
print(Dead_str, end='')
print('>')