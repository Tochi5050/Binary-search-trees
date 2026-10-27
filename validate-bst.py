# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

n1 = TreeNode(5)
n2 = TreeNode(4)
n3 = TreeNode(6)
n6 = TreeNode(3)
n7 = TreeNode(7)
# n8 = TreeNode(0)


# Connect left and right children
n1.left = n2
# n2.left = n8
n1.right = n3
n3.left = n6
n3.right = n7
root = n1


class Solution:
    def __init__(self):
        self.left_highest = [float("-inf")]
        self.right_lowest = [float("inf")]
    def isValidBST(self, root: TreeNode | None, pos) -> bool:
        if root is None:
            return []

        self.isValidBST(root.left, "left")
        self.isValidBST(root.right, "right")

        print(root.val, pos)






result = Solution()
print(result.isValidBST(root, "top"))
