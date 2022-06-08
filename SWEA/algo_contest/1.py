

#[위치, 존재하는 그물들, 현재 채력]  # 이동할 좌표 넣으면, 존재하는 그물들 이용해서, 해당 부분의 그물게이지 구해야함
import sys
sys.stdin = open('input1.txt')

T = int(input())
for t in range(1,T+1):
    N, M, K = map(int,input().split()) # N : 배열크기, M : 그물 개수, K 아기상어 체력
    sr, sc = map(int,input().split()) # 1 ~ N
    tr, tc = map(int,input().split()) # 1 ~ N

    sr -= 1
    sc -= 1
    tr -= 1
    tc -= 1
    # print('시작,끝',(sr,sc),(tr,tc))
    nets = {net_num : [set(),0] for net_num in range(M)} # 그물 번호 : [(그물이 가진 칸들), 그물강도]

    def make_nets(r,c,d,p,net_num):

        for i in range(-d,d+1): # -d, ... -1, 0, 1, 2, ..., d
            width = 2*d+1 - 2*abs(i)
            half_width = width//2 + 1  # 1, 2, 3

            for j in range(-half_width+1, half_width): # -half_width+1, ..., 0, half_width-1
                nr, nc = r + i, c + j
                if 0 <= nr < N and 0 <= nc <N:
                    nets[net_num][0].add((nr,nc))

        nets[net_num][1] = p


    for net_num in range(M):

        r, c, d, p = map(int,input().split())  # 그물 중심, 길이, 강도

        r -= 1
        c -= 1
        make_nets(r,c,d,p,net_num)
    # print(nets)


    def get_p(r,c,*c_nets):
        p = 0
        n_nets = list(c_nets)
        for net in list(c_nets):
            # print(c_nets)
            if (r,c) in nets[net][0]:
                p += nets[net][1]
                n_nets.remove(net)
        return p , n_nets






    visited = [ [[0]*N for _ in range(N)] for _ in range(K+1)]  # visited[k] 는 체력이 k일 때 방문여부



    q = [[sr,sc, list(range(M)),K ,1]]
    visited[K][sr][sc] = 1
    flag = False
    while q:
        # print('q is : ', q)
        cr, cc, c_nets, c_k, c_move = q.pop(0)
        c_nets = c_nets.copy()

        if cr == tr and cc == tc :
            print(f'#{t} {c_move-1}')
            flag = True
            break

        for move in ([-1,0],[1,0],[0,1],[0,-1]):
            nr = cr+move[0]
            nc = cc+move[1]

            np, n_nets = get_p(nr,nc,*c_nets)
            n_k = c_k - np
            # print('cur info1 : ',  nr,nc,n_nets,n_k,c_move+1)

            if 0 <= nr < N and 0 <= nc < N and n_k> 0 and visited[n_k][nr][nc]==0 :
                # print('cur info2 : ', nr, nc, n_nets, n_k, c_move + 1)
                q.append([nr,nc,n_nets,n_k, c_move+1])
                visited[n_k][nr][nc] = c_move+1






    if flag == False:
        print(f'#{t} -1')

    # print('================================================')













