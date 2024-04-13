class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_turned_on = 0  # Track the maximum turned-on bulb
        count = 0 
        for i, num in enumerate(flips, 1):
            max_turned_on = max(max_turned_on, num)  # Update the maximum turned-on bulb
            if max_turned_on == i:  # Check if all bulbs before max_turned_on are turned on
                count += 1 
        return count