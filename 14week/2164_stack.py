import sys
sys.stdin = open('2164_input.txt', 'r')

n = int(input())
Queue = []

for i in range(1,n+1):
    Queue.append(i)

while len(Queue) != 1:
    Queue.pop(0)
    t2 = Queue.pop(0)

    Queue.append(t2)

print(Queue[0])