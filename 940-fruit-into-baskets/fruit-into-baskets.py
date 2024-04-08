class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        left = 0 
        maximum = 1
        for indx in range(len(fruits)):
            count[fruits[indx]] = 1 + count.get(fruits[indx], 0)
            while len(count) > 2:
                count[fruits[left]] -= 1
                if  count[fruits[left]] == 0 :
                    count.pop(fruits[left])
                left += 1
            maximum = max ( maximum,indx- left +1)
        return maximum

        