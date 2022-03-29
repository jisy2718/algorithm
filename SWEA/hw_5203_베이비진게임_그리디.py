def discrimination(c):
    for i in range(10):
        # 3개 같은 수
        if c[i] >= 3:
            return True
        # 3개 연속된 수
        if 0 <= i < 8 and 0 < c[i] < 3 and 0 < c[i + 1] < 3 and 0 < c[i + 2] < 3:
            return True
    return False

T = int(input())
for tc in range(1,T+1):

    cards = list(map(int,input().split()))
    p1 = [cards[i] for i in range(0,len(cards),2) ]
    p2 = [cards[i] for i in range(1,len(cards),2) ]



    c1 = [0] * 10
    c2 = [0] * 10

    for i in range(6):
        c1[p1[i]] += 1
        r1 = discrimination(c1)
        # print(f"c1 : {c1}")
        c2[p2[i]] += 1
        r2 = discrimination(c2)
        # print(f"c2 : {c2}")
        if r1 == True :
            print(f"#{tc} {1}")     # player1이 이긴 경우
            break
        elif r2 == True:     # player2가 이긴 경우
            print(f"#{tc} {2}")
            break
    else: # 비긴 경우
        print(f"#{tc} {0}")
        





























