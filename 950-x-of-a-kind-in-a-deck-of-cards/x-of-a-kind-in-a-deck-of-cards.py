class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        counts = list(count.values())
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        gcd_value = counts[0]
        for count in counts[1:]:
            gcd_value = gcd(gcd_value, count)
        
        return gcd_value >= 2