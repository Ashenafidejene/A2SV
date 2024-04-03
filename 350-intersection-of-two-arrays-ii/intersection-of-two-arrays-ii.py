class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = []
        for i in range(len(nums1)):
            if nums1[i] in nums2 :
                count.append(nums1[i])
                nums2.remove(nums1[i])
        return count