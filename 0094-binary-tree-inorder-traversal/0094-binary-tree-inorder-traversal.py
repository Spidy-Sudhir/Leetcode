# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inor(self, root):
#         ans=[]
#         if root==None:
#             return
#         ans.append(self.inor(root.left))
#         ans.append(self.inor(root.right))
#         return ans
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         self.inor(root)

class Solution:
    def inor(self, root, ans):
        if root is None:
            return
        
        self.inor(root.left, ans)   # left
        ans.append(root.val)        # root
        self.inor(root.right, ans)  # right

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.inor(root, ans)
        return ans
