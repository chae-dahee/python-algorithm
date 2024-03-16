Queue=[]

for people in range(1,42):  #큐에 값 집어넣음
    Queue.append(people)

while len(Queue) != 2:  #남은수가 2가 아닌동안
    alive1 = Queue.pop(0)
    alive2 = Queue.pop(0)
    dead = Queue.pop(0)

    Queue.append(alive1)
    Queue.append(alive2)
    #첫번째 두번째 살고, 세번째 제거... 살아남은 두명을 맨 뒤에 넣어줌. 2명 남을때까지 반복

print(Queue)    #2명 남아서 반복문 탈출, 큐 전체출력