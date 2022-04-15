#Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: list()) -> TreeNode:
        l=len(nums)
        if l==0:
            return
        if l==1:
            return TreeNode(nums[0])
        p=max(nums)
        position=nums.index(p)
        root=TreeNode(p)
        root.left=self.constructMaximumBinaryTree(nums[0:position])
        root.right=self.constructMaximumBinaryTree(nums[position+1:l])
        return root
        