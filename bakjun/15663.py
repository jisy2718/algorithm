N, M = map(int,input().split())

arr = list(map(int,input().split()))

arr.sort()
p = [0]*M
printed = set()
def perm(idx, used):

    if idx == M:
        cur = ''.join((str(e) for e in p))
        # 중복되지 않는다면 출력
        if cur not in printed:
            print(*p)
            printed.add(cur)
        return


    else:
        for i in range(N):
            if i not in used:  # 사용하지 않은 index i이면 사용하기.
                p[idx] = arr[i]
                used.add(i)
                perm(idx+1,used)
                used.remove(i)

used=set()
perm(0,used)