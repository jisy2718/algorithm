# 완전이진트리에서 순회
# 자식 노드가 존재하는 경우에만 순회하는 경우
# (pre_in_post_order_traversal.py) 파일은 우선 자식 방문해서, 존재하는지 확인
def pre_order(v):
    global last
    if v <=last: # 마지막 정점번호 이내
        print(v)
        pre_order(v*2) # 왼자식
        pre_order(v*2 + 1) # 오른자식