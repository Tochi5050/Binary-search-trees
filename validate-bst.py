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
        self.hashMap = {}
    def isValidBST(self, root: TreeNode | None, pos) -> bool:

        if root is None:
            return True

        self.hashMap[root] = root.val

        if self.isValidBST(root.left, "left") and self.isValidBST(root.right, "right"):
            if root.left is not None and root.right is not None:
                if self.hashMap[root.left] < self.hashMap[root] and self.hashMap[root.right] > self.hashMap[root] and pos == "left":
                    self.hashMap[root] = self.hashMap[root.right]
                    return True

                elif self.hashMap[root.left] < self.hashMap[root] and self.hashMap[root.right] > self.hashMap[root] and pos == "right":
                    self.hashMap[root] = self.hashMap[root.left]
                    return True

                else:
                    return False

            elif root.left is not None and root.right is None:
                if self.hashMap[root.left] < self.hashMap[root] and pos == "left":
                    self.hashMap[root] = self.hashMap[root.right]
                    return True
                elif self.hashMap[root.left] < self.hashMap[root] and pos == "right":
                    self.hashMap[root] = self.hashMap[root.left]
                    return True
                else:
                    return False

            elif root.left is None and root.right is not None:
                if self.hashMap[root.right] > self.hashMap[root] and pos == "left":
                    self.hashMap[root] = self.hashMap[root.right]
                    return True
                elif self.hashMap[root.right] > self.hashMap[root] and pos == "right":
                    self.hashMap[root] = self.hashMap[root.left]
                    return True
                else:
                    return False
            else:
                return True

        return False




result = Solution()
print(result.isValidBST(root, "left"))
