class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        counter = set()
        left = 0 
        mins = len(cards) + 1
        
        for right in range(len(cards)):
            while cards[right] in counter:
                mins = min(mins, right - left + 1)
                counter.remove(cards[left])
                left += 1 
            counter.add(cards[right])
        
        return mins if mins != len(cards) + 1 else -1 