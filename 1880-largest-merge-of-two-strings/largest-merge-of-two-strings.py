class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = ""
        i=0
        l=0
        while len(word1) > i and len(word2) > l:
            if word1[i:] > word2[l:]:
                merge += word1[i]
                i+=1
            else:
                merge += word2[l]
                l+=1
        
        if i < len(word1):
            merge+=word1[i:]
        if l < len(word2):
            merge += word2[l:]
        return merge 