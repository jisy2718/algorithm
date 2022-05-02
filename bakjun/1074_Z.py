def divide(n,x,y,r,c):# 왼쪽위 꼭지점이 x행 y열이고, 길이가 n 인 박스
    global result

    # 1개 남은 경우, 자기 자신만 순서에 더해주면 되는줄 알았는데, 시작을 1개 포함해서 안세어도 됨
    if n == 1:
        return

    # 4 등분 시작
    # 1. 왼쪽 위인 경우
    if x <=c< x + n//2 and y <= r < y + n//2:
        result += 0
        divide(n//2,x,y,r,c)


    # 2. 오른쪽 위인 경우
    elif x + n//2 <= c < x + n and y <=r  < y + n//2:
        result += (n//2)**2
        divide(n//2, x + n//2, y ,r ,c)


    # 3. 왼쪽 아래인 경우
    elif x <= c < x + n//2 and y + n//2 <= r < y + n:
        result += 2*( (n//2)**2 )
        divide(n//2, x, y + n//2 ,r ,c)


    # 4. 오른쪽 아래인 경우
    elif x + n//2 <= c < x + n and y + n//2 <= r < y + n:
        result += 3* ( (n//2)**2 )
        divide(n//2, x + n//2, y + n//2, r, c)





N, tr, tc = map(int,input().split())

# 4등분했을 때, 왼위, 오위, 왼아래, 오아래 중 어디인지 계속파악해서 개수 더해주면 됨. 이 때 n == 1 되면 끝


result = 0
divide(2**N,0,0,tr,tc)
print(result)