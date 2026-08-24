# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def helper(root, string):
            if root.left is None and root.right is None:
                string += str(root.val)
                ans.append(string)
                return

            string += str(root.val) + "->"

            if root.left:
                helper(root.left, string)

            if root.right:
                helper(root.right, string)

        helper(root, "")
        return ans