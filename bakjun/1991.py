N = int(input())

tree = {}
for _ in range(N):
    p, c1, c2 = input().split()
    tree[p] = [c1, c2]


def traversal(v, order):
    if v == '.':
        return

    if order == "pre":
        print(v, end='')

    traversal(tree[v][0], order)

    if order == "in":
        print(v, end='')

    traversal(tree[v][1], order)

    if order == "post":
        print(v, end='')


traversal('A', 'pre')
print()
traversal('A', 'in')
print()
traversal('A', 'post')