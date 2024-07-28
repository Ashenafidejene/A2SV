# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def dfs (node1 ,arr):
            if not node1 :
               return 
            dfs(node1.left,arr)
            arr.append(node1.val)
            dfs(node1.right,arr)
        arr1 = []
        arr2 = []
        dfs(root1,arr1)
        dfs(root2,arr2)
        ans = []
        i = 0 
        l = 0
        while i < len(arr1) and l < len(arr2):
            if arr1[i]<arr2[l]: 
                ans.append(arr1[i])
                i+=1
            else:
                ans.append(arr2[l])
                l+=1 
        if i < len(arr1):
            ans.extend(arr1[i:])
        if  l < len(arr2):
           ans.extend(arr2[l:])
        return ans 


             