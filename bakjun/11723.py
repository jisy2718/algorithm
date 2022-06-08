M = int(input())

S = set()

for _ in range(M):
    ind = input().split()

    if ind[0] == "all":
        S = set(range(1,21))

    elif ind[0] == "empty":
        S = set()

    elif ind[0] == "add":
        S.add(int(ind[1]))

    elif ind[0] == "toggle":
        num = int(ind[1])
        if num in S:
            S.remove(num)
        else:
            S.add(num)

    elif ind[0] == "remove":
        num = int(ind[1])
        if num in S:
            S.remove(num)

    elif ind[0] == "check":
        if int(ind[1]) in S:
            print(1)
        else:
            print(0)