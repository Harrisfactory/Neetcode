# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        #first value in preorder is our root, then we find it in inorder and thats our left right slice

        #base case, do we have any nodes
        if not preorder or not inorder:
            return None
        
        #set root
        root = TreeNode(preorder[0])
        #find root in inorder for split
        mid = inorder.index(root.val)
        #construct left
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid+1:])

        return root
