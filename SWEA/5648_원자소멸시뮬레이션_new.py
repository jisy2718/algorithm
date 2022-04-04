
# 이동 / 상하좌우
dr = [1,-1,0,0]
dc = [0,0,-1,1]


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    energe = 0
    arr = []
    for _ in range(N):
        # 좌표 x2배
        element = list(map(int,input().split()))
        element[0] = element[0]*2
        element[1] = element[1]*2
        arr.append(element)


    # 4000회 loop 반복
    # 1번 이동 후 위치 같아지면 소멸

    for loop in range(4000):
        used = set()
        crash = set()
        for i in range(len(arr)-1,-1,-1):
            d = arr[i][2]
            arr[i][0] = arr[i][0] + dc[d]
            arr[i][1] = arr[i][1] + dr[d]

            if (arr[i][0],arr[i][1]) not in used:
                used.add((arr[i][0],arr[i][1]))

            else:
                crash.add((arr[i][0],arr[i][1]))



        for i in range(len(arr)-1,-1,-1):
            if (arr[i][0], arr[i][1]) in crash:
                energe += arr.pop(i)[3]

        if len(arr) == 1:
            break

    print(f"#{tc} {energe}")


