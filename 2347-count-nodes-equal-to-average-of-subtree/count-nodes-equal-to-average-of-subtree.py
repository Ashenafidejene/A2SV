# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0 
        def dfs(node):
            if not node :
                return (0,0)
            if not (node.left or node.right):
                self.count +=1
                return (1,node.val)
            (leftNumber , leftValue) = dfs(node.left)
            (rightNumber , RightValue)=dfs(node.right)
            totalSum = leftValue+RightValue + node.val
            totalNumber = leftNumber + rightNumber  + 1 
            if( node.val == (totalSum // totalNumber) ):
                self.count +=1
            return (totalNumber,totalSum)
        dfs(root)
        return self.count

        