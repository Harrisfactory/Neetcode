# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, trackedSum: int = 0) -> bool:
        
        #check that there is a root at all
        if root:
            #first take the current nodes value and add it to our running sum
            trackedSum += root.val

            #check if we are at a lead node
            if root.left is None and root.right is None:
                #at a leaf node, do we hit our target?
                if trackedSum == targetSum:
                    return True
                
            
            return self.hasPathSum(root.left, targetSum, trackedSum) or self.hasPathSum(root.right, targetSum, trackedSum)
