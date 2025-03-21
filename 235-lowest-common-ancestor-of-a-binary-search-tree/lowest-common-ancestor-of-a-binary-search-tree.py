# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack1 = []
        stack2 = []
        def finder(root,stack,val):
            if not root:
                return stack
            stack.append(root)
            if root.val == val :
                return stack
            
            if root.val > val:
                return finder(root.left,stack[:],val)
            else:
                return finder(root.right,stack[:],val)
        
        stack1 = finder(root,[],p.val)
        stack2 = finder(root,[],q.val)
        while stack1 and stack2:
            if stack1[-1] == stack2[-1]:
                return stack1[-1]
            if len(stack1) > len(stack2):
                stack1.pop()
            elif len(stack1) <len(stack2):
                stack2.pop()
            else:
                stack1.pop()
                stack2.pop()
        return None

        