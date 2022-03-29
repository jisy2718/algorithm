N = int(input())

tree = {}  # { node : {child:weight} }
visited = {}
for _ in range(N - 1):
    p, c, w = map(int, input().split())
    if p in tree:
        tree[p][c] = w
    else:
        tree[p] = {c: w}
    if p not in visited:
        visited[p] = False
    if c not in visited:
        visited[c] = False

    # ------------------------------
def post(v):
    result = 0
    if v not in tree:
        return result

    v_results = []
    for child in tree[v]:
        v_results.append(post(child)+tree[v][child])
    v_results.sort()
    if len(v_results) >= 2:
        results.append(v_results[-1]+v_results[-2])


    return max(v_results)

results = []
post(1)
print(max(results))


stack = [1]
results = []


def post(v):
    stack = [v]
    visited[v]=True
    results = []
    while stack:
        cur = stack.pop()

        # 자식이 있으면 stack에 추가
        if cur in tree:
            for child in tree[cur]:
                if visited[child]==False:
                    visited[child] = True
                    results.append(tree[cur][child])

        else:











# def dfs(s, e, weight_sum):
#     weight = tree[s][e]
#     if e not in tree:
#         c_results.append(weight_sum + weight)
#     else:
#         for c in tree[e]:
#             if root_visited[c] == False:
#                 # print(f"node {e} to {c}")
#                 root_visited[c] = True
#                 dfs(e, c, weight_sum + weight)
#     return
#
#
# results = []
# for root in tree:
#     root_results = []
#     root_visited = copy.deepcopy(visited)
#     for c in tree[root]:
#         c_results = []
#         dfs(root, c, 0)
#         root_results.append(max(c_results))
#
#     if len(root_results) >= 2:
#         root_results.sort()
#         results.append(root_results[-1]+root_results[-2])
#         # print(f"root is {root} results {root_results[-1]} {root_results[-2]}")
# print(max(results))
#
#
#
