# 1. 부분집합
arr = [1,2,3,4,5]
n = len(arr)

for i in range(1<<n):
    # result = []
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end=' ')
    print()
print('------------------')
# 2. 순열
arr = [1,2,3]
n = len(arr)
used=[0]*n
result = [0]*n
def perm(idx):
    if idx == n:
        print(result)
    else:
        for i in range(n):
            if used[i] == 0:
                used[i] = 1
                result[idx] = arr[i]
                perm(idx+1)
                used[i] = 0
perm(0)

print('-------------------------')
# 3. 조합 nCr
arr = [1,2,3,4,5]
n = len(arr)
r = 3
used=[0]*n

def nCr(idx, k):
    if k == r:
        print(used)
        # for i in range(n):
        #     if used[i] == 1:
        #         print(arr[i], end=' ')
        # print()
    if idx >= n:
        return

    used[idx] = 1
    nCr(idx+1, k+1)
    used[idx] = 0
    nCr(idx+1, k)

nCr(0,0)