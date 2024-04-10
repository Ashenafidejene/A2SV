class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxs = max(costs)
        counter = 0
        cloneCoin = coins
        nums = [0] * (maxs + 1)
        
        for num in costs:
            nums[num] += 1
            
        for i in range(len(nums)):  # Loop through the nums array
            for j in range(nums[i]):
                cloneCoin -= i
                if cloneCoin < 0:  # Corrected comparison
                    return counter
                counter += 1
                
        return counter