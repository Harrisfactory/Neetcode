# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        #do inorder traversal then get kth element

        inorderArr = []

        def inorder(root):

            if root is None:
                return

            inorder(root.left)
            inorderArr.append(root.val)
            inorder(root.right)
        inorder(root)

        return inorderArr[k-1]
