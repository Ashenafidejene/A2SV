class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count = {}
        temp = []
        for x in arr:
            count[(((x % k) + k) % k)] = 1 + count.get((((x % k) + k) % k),0)
            temp.append((((x % k) + k) % k))
        for val in temp:
            if val in count:
                if val == 0:
                    if count[val] % 2 == 0:
                        count.pop(val)
                    else:
                        return False
                else:
                    count[val]-=1
                    if count[val] == 0:
                        count.pop(val)
                    if k - val in count:
                        count[k - val] -= 1
                        if count[k - val] == 0:
                                count.pop(k - val)
                    else:
                        return False
        return len(count) == 0 
                   

        
