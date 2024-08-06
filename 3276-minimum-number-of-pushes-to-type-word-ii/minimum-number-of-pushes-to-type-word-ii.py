class Solution:    
    def minimumPushes(self, word: str) -> int:
        # Count the frequency of each character
        freq = Counter(word)
        
        # Sort characters by frequency
        sorted_chars = sorted(freq.elements(), key=lambda ch: freq[ch],reverse=True)
        
        unique_count = set()
        total_pushes = 0
        incrementer = 1
        
        for ch in sorted_chars:
            if ch in unique_count:
                total_pushes += incrementer
            else:
                unique_count.add(ch)
                if len(unique_count) == 9:
                    incrementer += 1
                    unique_count = set()
                    unique_count.add(ch)
                total_pushes += incrementer
                
        return total_pushes