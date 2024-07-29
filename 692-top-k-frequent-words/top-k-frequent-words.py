class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        count = Counter(words)   
        ans = [item for item, freq in count.most_common(k)]
        return ans 