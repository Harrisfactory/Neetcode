# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        #check breaks first
        if not p and not q:
            return True

        if (p and not q) or (not p and q):
            return False
        
        if p.val != q.val:
            return False
    
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        #explained since we want to check each element from the top down I chose preorder
        #if both nodes are empty, they are the same so recursivly that is True,
        #otherwise if either are empty but not both OR their values arent the same, thats false recursivly
        #then we do that same check as we traverse down the tree
