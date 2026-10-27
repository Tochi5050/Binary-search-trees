class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

n1 = TreeNode(4)
n2 = TreeNode(7)
n3 = TreeNode(6)
n4 = TreeNode(8)
n5 = TreeNode(5)
n6 = TreeNode(9)

n1.right = n2
n2.left = n3
n2.right = n4
n3.left = n5
n4.right = n6

class Solution:
    def __init__(self):
        self.tree = []
    def inorderTraversal(self, root):
        if root is None:
            return

        self.inorderTraversal(root.left)
        self.tree.append(root.val)
        self.inorderTraversal(root.right)

    def preprocessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNodeHelper(self, root, key):
        if root is None:
            return None

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        self.deleteNodeHelper(root, key)
        return self.tree

result = Solution()
root = n1
key = 7
print(result.deleteNode(root, key))
