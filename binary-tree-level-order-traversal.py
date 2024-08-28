# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = []

        q = [root]

        while len(q) > 0:
            level = []
            #iterate through the current queue
            for i in range(len(q)):
                node = q.pop(0)

                #process current node if not null
                if node:
                    level.append(node.val)
                    #add children of node to the queue
                    q.append(node.left)
                    q.append(node.right)
            if len(level) > 0:
                result.append(level)

        return result 

        #O(n)
