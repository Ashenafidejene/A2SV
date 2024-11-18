class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res = [0]*len(deck)
        q = deque(range(len(deck)))
        for d in deck :
            i = q.popleft()
            res[i]= d 
            if q : 
                q.append(q.popleft())
        return res
