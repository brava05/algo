# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True
MAX_NUMBER = None
if LOCAL:
    class Node:  
        def __init__(self, value, left=None, right=None):  
            self.value = value  
            self.right = right  
            self.left = left

def check_tree(root):
    if root is None:
        return

    global MAX_NUMBER
    # print(root.value)
    if MAX_NUMBER is None:
        MAX_NUMBER = root.value
    if MAX_NUMBER < root.value:
        MAX_NUMBER = root.value


    check_tree(root.right)
    check_tree(root.left)


def solution(root):
    check_tree(root)
    return MAX_NUMBER


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3

if __name__ == '__main__':
    test()
