# 최대 100개의 정수가 키로 입력될 때

# 1. 최대힙 구현

def enq(n):
    global last
    last += 1
    tree[last] = n  # 완전이진트리 유지

    # 최대힙으로 맞춰주기
    child = last
    parent = child // 2  # 완전이진트리의 부모 정점번호
    while tree[parent] < tree[child] and parent >= 1:  # 자식 키값 더 큰 경우
        tree[parent], tree[child] = tree[child], tree[parent]  # 위치바꾸기
        child = parent
        parent = child // 2

def deq(): # 삭제
    global last
    tmp = tree[1]
    tree[1] = tree[last]
    last -= 1
    #--------삭제 후, 자리 바꾸기 끝
    # ------- 최대힙 유지를 위해 부모>자식 여부 파악 후 교환
    parent = 1
    left_child = parent * 2 # 왼쪽 자식
    cur_child = left_child   # cur_child는 현재 왼쪽자식
    right_child = left_child + 1
    while cur_child <= last: # 비교할 자식이 있다면
        # 오른쪽 자식도 있고, 오른쪽 자식이 왼쪽 자식보다 더 크다면
        if right_child <= last and tree[left_child] < tree[right_child]:
            cur_child = right_child  # right child 와 parent 비교

        if tree[parent] < tree[cur_child]: # 자식 키 값이 더 크면 교환
            tree[parent], tree[cur_child] = tree[cur_child], tree[parent]
            # parent 바꾸기
            parent = cur_child
            cur_child = parent*2
        else:
            break
    return tmp





# 완전이진트리 정점 1 ~ 100
V = 100
tree = [0]*(V+1)

# 마지막 정점 번호 관리
last = 0

enq(3)
enq(2)
enq(4)
enq(7)
enq(5)
enq(1)
# print(tree[1])
enq(9)
# print(tree[1])
while last > 0:
    print(deq(), tree[1])
