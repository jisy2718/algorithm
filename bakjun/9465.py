T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(2)]

    # 아래 6가지 경우가 가능함.
    # sij 는 (j,i)를 선택한 상태까지의 최대합
    # aij 는 (j,i)에서의 값

    # # ?XO
    # # XOX 꼴
    # si1 = ai1 + s_{i-1}{2}
    #
    # # XXO
    # # OXX 꼴
    # si1 = ai1 + s_{i-2}(2)
    #
    #
    # # OXO
    # # XXX 꼴
    # si1 = ai1 + s_{i-2}{1}
    #
    #
    # # XOX
    # # ?XO 꼴
    # si2 = ai2 + s_{i-1}{1}
    #
    # # OXX
    # # XXO 꼴
    # si2 = ai2 + s_{i-2}{1}
    #
    # # XXX
    # # OXO
    # si2 = ai2 + s_{i-2}{2}

    if N == 1:
        print(max(arr[0][0],arr[1][0]))

    else:
        srr = [[0]*N for _ in range(2)]

        srr[0][0] = arr[0][0]
        srr[1][0] = arr[1][0]

        # XO
        # OX
        srr[0][1] = srr[1][0] + arr[0][1]

        # OX
        # XO
        srr[1][1] = srr[0][0] + arr[1][1]


        for i in range(2,N):
            srr[0][i] = arr[0][i] + max(  srr[1][i-1] , srr[1][i-2] , srr[0][i-2]  )
            srr[1][i] = arr[1][i] + max( srr[0][i-1], srr[0][i-2], srr[1][i-2]  )

        print(max(max(srr[0]), max(srr[1])))















