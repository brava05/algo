# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"val: {self.val}, left: {self.left}, right: {self.right}"

    def __str__(self) -> str:
        return str(self.val)

class Solution:
    def mergeTrees(self, root1, root2):
        
        if root1 is None:
            # вместо None поставил root1, чтобы в ответ выгружался null а не None
            return root2 if root2 is None else TreeNode(root2.val) 
        if root2 is None:
            return root1 if root1 is None else TreeNode(root1.val)

        node = TreeNode(root1.val + root2.val)
        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)

        return node

    def mergeTrees_True(self, root1, root2):
        
        if root1 is None:
            return TreeNode(None if root2 is None else root2.val)
        if root2 is None:
            return TreeNode(None if root1 is None else root1.val)

        node = TreeNode(root1.val + root2.val)
        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)

        return node

    def mergeTrees_leetCode(self, root1, root2):
        
        if root1 is None:
            return root2
        if root2 is None:
            return root1

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1

def to_binary_tree(items: list[int]) -> TreeNode:
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()

Sol = Solution()
root1 = to_binary_tree([1,3,2,5])
root2 = to_binary_tree([2,1,3,None,4,None,7])
print(Sol.mergeTrees(root1, root2).__repr__())






# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]
# Example 2:

# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]