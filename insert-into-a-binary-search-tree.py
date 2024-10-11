# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root:

            #if root is greater, check if there is a left opening, if not then move left

            #if root is lesser, check if there is a right opening, if not then move right

            cur = root

            while cur:
                #current node is greater than our target
                if cur.val > val:
                    #check left for opening to insert
                    if cur.left is None:
                        cur.left = TreeNode(val)
                        return root
                    #else move left
                    cur = cur.left
                else:
                    #check right for opening to insert
                    if cur.right is None:
                        cur.right = TreeNode(val)
                        return root
                    #else move right
                    cur = cur.right

        return TreeNode(val)
