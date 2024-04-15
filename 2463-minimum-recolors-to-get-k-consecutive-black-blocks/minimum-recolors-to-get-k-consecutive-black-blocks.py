class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = {'W':0,'B':0}
        left = 0 
        
        for indx in range(k):
            count[blocks[indx ]] +=1
        res = count['W']
        for right in range(k , len(blocks)):
            count[blocks[left]]-=1
            count[blocks[right]] +=1
            left+=1
            res = min (res , count['W'] )
        return res
        