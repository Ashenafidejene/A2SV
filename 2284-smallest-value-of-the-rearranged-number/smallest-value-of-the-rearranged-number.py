class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            num *= -1
            sd = str(num)
            sd = sorted(sd, reverse=True)  # Use sorted() function
            num = int(''.join(sd))  # Join the sorted 
            num *= -1
        else:
            sd = str(num)
            sd = sorted(sd)
            if sd[0] == '0':
                for i in range(1, len(sd)):  # Start from index 1
                    if sd[i] != '0':
                        sd[0], sd[i] = sd[i], sd[0]
                        break
            num = int(''.join(sd))  # Join the sorted characters
        
        return num