import sys
input = sys.stdin.readline

N = int(input())

heap = [0]*100001
loc = 0

def insert(new):
    global loc
    loc += 1
    heap[loc] = new

    # 부모와 비교해서 절대값 작은 것이 부모로 가야함
    child = loc
    if loc >1: # 부모가 존재한다면
        parent = loc//2
        while parent > 0 and abs(heap[child]) < abs(heap[parent]): # 부모가 존재할 때까지
            # if abs(heap[child]) < abs(heap[parent]):
            heap[child] , heap[parent] = heap[parent], heap[child]

            child = parent
            parent = parent//2


        # 절대값이 같은 경우
        while parent >= 1 and abs(heap[child]) == abs(heap[parent]):

            #  비교해서 작은 값을 부모로하기
            if heap[child] < heap[parent]:
                heap[child], heap[parent] = heap[parent], heap[child]

                child = parent
                parent = parent//2
            elif heap[child] == heap[parent]:
                break
    # print(f'insert {new} now heap is {heap}')


def delete():
    global loc
    # 이미 원소가 1개 이상 있는 경우
    if loc >= 1:
        result = heap[1]
        # print(result)
    # 원소가 없는 경우
    else:
        print(0)
        return

    # 마지막 원소와 위치 교환
    heap[1], heap[loc] = heap[loc], heap[1]
    loc -= 1
    
    # 자식 1, 2 존재하면 비교
    parent = 1
    c = parent*2
    # loc == 1이라면 원소 1개남아서 힙 정렬 끝난 것
    while loc > 1 and parent*2 <= loc:
        if c +1 <=loc:
            # 만약 오른쪽 것이 더 작다면 c 바꾸기
            if abs(heap[c]) > abs(heap[c+1]):
                c = c+1
            elif abs(heap[c]) == abs(heap[c+1]) and heap[c] > heap[c+1]:
                c = c+1
        # 이제 c 와 parent 비교해서 바꾸기
        if abs(heap[parent]) > abs(heap[c]):
            heap[parent], heap[c] = heap[c], heap[parent]
            parent = c
            c = parent * 2

        elif abs(heap[parent]) == abs(heap[c]) and heap[parent] > heap[c]:
            heap[parent], heap[c] = heap[c], heap[parent]
            parent = c
            c = parent*2
        # 부모와 자식간 교환이 안 일어나는 경우 break
        else:
            break
    # heap.pop()
    # print(f'now heap is {heap}')
    print(result)

for _ in range(N):
    x = int(input())
    if x == 0:
        delete()
    else:
        insert(x)


    



