class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l,r = 0, 0 
        edge1 = len(nums1)
        edge2 = len(nums2)
                    
        while l < len(nums1):
            if r!=len(nums2) and nums1[l]>=nums2[r]:
                nums1.insert(l,nums2[r])
                r+=1
            elif l >=(len(nums1)-len(nums2)-1) and nums1[l]==0 and r!=len(nums2):
                nums1[l]=nums2[r]
                r+=1
                l+=1
            elif nums1[l] == 0 and  l >=len(nums1)-len(nums2)-1 :
                nums1.pop()
            else:
                l+=1 
        for i in range(len(nums1), edge1):
            nums1.insert(nums1.index(0),0)

            
        