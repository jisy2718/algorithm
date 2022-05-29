arr = [1, 2, 3, 4, 5]
n = 5
r = 3
used= [0] *5

def comb( idx, cnt):
    if cnt == r:
        print(used)
        return

    if idx >= n:
        return

    used[idx] = 1
    comb(idx + 1, cnt + 1)
    used[idx] = 0
    comb( idx + 1, cnt)



comb(0,0)