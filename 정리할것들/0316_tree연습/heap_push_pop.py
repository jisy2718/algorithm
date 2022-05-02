level = 3

# 최대 힙
heap = [0] * 2**(level+1)
last = 0 # 마지막 요소를 가리키는 변수
def heap_push(value):
    global last
    # 완전이진트리 유지 위해서, 마지막 자리 넣어주기
    last += 1
    heap[last] = value

    # 마지막 자리에 넣은 후, 부모노드와 비교해 자리바꾸기
    parent_idx = last//2
    cur_idx = last

    # 자신이 root가 되면 멈추기 /  비교조건 맞을 때까지 진행
    while cur_idx > 1 and heap[parent_idx] < heap[cur_idx]:
        # 조건에 맞도록 바꾸기
        heap[parent_idx] , heap[cur_idx] = heap[cur_idx], heap[parent_idx]

        cur_idx = parent_idx
        parent_idx = cur_idx//2



heap_push(7)
print(heap)

heap_push(2)
print(heap)

heap_push(4)
print(heap)

heap_push(3)
print(heap)

heap_push(1)
print(heap)

heap_push(6)
print(heap)

heap_push(5)
print(heap)

heap_push(8)
print(heap)



def heappop():
    global last
    result = heap[1]
    # 마지막 요소를 올림
    heap[1] = heap[last]
    last -= 1

    # 비교 시작
    parent = 1
    cur_child = parent*2 # 좌측노드 우선 선정

    # 좌,우 자식 비교해서 child 결정
    # 오른쪽 자식이 있고, 왼쪽 자식보다 더 크다면
    if cur_child + 1 <= last and heap[cur_child] < heap[cur_child + 1]:
        cur_child += 1
    # cur_child 는 자식 중에 더 큰 값을 가지는 child의 idx

    while cur_child <= last and heap[cur_child] > heap[parent]:
        heap[cur_child] , heap[parent] = heap[parent], heap[cur_child]

        parent = cur_child
        cur_child =  parent * 2
        if cur_child + 1 <= last and heap[cur_child] < heap[cur_child + 1]:
            cur_child += 1
    return result


print(heappop())
print(heappop())
print(heappop())
print(heappop())
print(heappop())
print(heappop())
print(heappop())
print(heappop())
print(heap)
print(last)
print(heappop())
