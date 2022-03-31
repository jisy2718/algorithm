class Tree():
    def __init__(self,root):
        self.root = root


    def add_node(self,parent_val,child_val):
        parent_node = self.find(self.root, parent_val)
        if parent_node.left == None:
            parent_node.left = Node(child_val)
        elif parent_node.left and parent_node.right == None:
            parent_node.right = Node(child_val)
        else:
            print("parent 노드의 자식이 가득차서, 추가할 수 없습니다.")


    # node add
    def find(self,cur_node, target_val):
        # base case
        # if cur_node == None:
        #     return

        if cur_node.val == target_val:
            return cur_node

        else: # 자식 노드 검색
            if cur_node.left:
                result =  self.find(cur_node.left, target_val)
                if result!=None:
                    return result
            if cur_node.right:
                result =  self.find(cur_node.right, target_val)
                if result!=None:
                    return result


    def pre_order(self, cur_node):
        print(cur_node.val)
        if cur_node.left:
            self.pre_order(cur_node.left)
        if cur_node.right:
            self.pre_order(cur_node.right)








class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(1)
n2 = Node(2)
n3 = Node(3)
root.left = n2
root.right = n3
n4 = Node(4)
n5 = Node(5)
n2.left = n4
n2.right = n5
n6 = Node(6)
n7 = Node(7)
n3.left = n6
n3.right = n7
Nodes = [None,root,n2,n3,n4,n5,n6,n7]
for i in range(8,32):
    p = Nodes[i // 2]
    cur = Node(i)
    # print(f"parent values is {p.val}")
    if i % 2 == 0: # 짝수
        p.left = cur
        Nodes.append(cur)

    else:
        p.right =cur
        Nodes.append(cur)
print(Nodes)
print(len(Nodes))

T = Tree(root)
# T.add_node(3,10)
T.pre_order(root)
# print(root.left.left.left.val)


#
# check = T.find(root,10)
# print(check.val)
