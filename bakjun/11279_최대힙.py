

def delete():
    global last
    root = tree[1]
    tree[1] = tree[last]
    last -= 1

    p = 1
    c = 1*2
    # parent, 좌child, 우child 중 가장 큰 것이 parent로 와야 함
    while c <= last :
        if c+1 <= last and tree[c] < tree[c+1]: # 오른쪽 자식 존재하고, 오른쪽 자식이 왼쪽자식보다 더 크면
            c = c + 1

        if tree[c] > tree[p]:
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = p*2
        else:
            break
    return(root)

def insert(new):
    global last

    last += 1
    tree[last] = new


    c = last
    p = last//2
    # print(f"c {c}, p {p}, last {last}")
    while p >= 1 and tree[c] > tree[p]: # 부모가 존재하고, 자식이 더 크면 swap
        tree[c], tree[p] = tree[p], tree[c]
        c = p
        p = c//2



N = int(input())
# root가 1부터 시작
last = 0
tree = [0]*(N+1) # 1 부터 이용
orders = [0]*N
for i in range(N):
    new = int(input().strip())
    orders[i] = new

for new in orders:
    if new == 0:
        if last > 0: # heap에 원소 존재하면
            result = delete()
            print(result)
        else:
            print('0')
    else:
        insert(new)




