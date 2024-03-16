import sys
sys.stdin = open('10773_input.txt', 'r')

k = int(input())
Queue=[]

for i in range(k):
    n = int(input())
    if n != 0:
        Queue.append(n)
    else:
        Queue.pop(-1)

print(sum(Queue))