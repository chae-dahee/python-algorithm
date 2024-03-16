#import sys
#sys.stdin = open('DFS-input.txt', 'r')

Queue=[]    #Queue:[1,2,3,4]

# Queue.append(1)
# Queue.append(2)
# Queue.append(3)
# Queue.append(4)

for now in range (1,5):
    Queue.append(now)

# print(Queue.pop(0))     #1 Queue에서 나왔기 때문!
# # print(Queue)    #[2,3,4] ->앞으로 땡겨짐
# print(Queue.pop(0))     #2 Queue에서 나왔기 때문!
# # print(Queue)    #[3,4]
# print(Queue.pop(0))
# print(Queue.pop(0))

while Queue:    #Queue안에 값이 있는 동안
    print(Queue.pop((0)))   #1\2\3\4