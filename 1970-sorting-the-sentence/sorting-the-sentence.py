class Solution:
    def sortSentence(self, s: str) -> str:
        stores = []
        start = 0
        for i in range(len(s)):
            if s[i].isdigit():
                stores.append([int(s[i]), start, i - 1])
                start = i + 2
        
        stores.sort()
        final = ""
        for i in range(len(stores)):
            for j in range(stores[i][1], stores[i][2] + 1):
                final += s[j]
            if i != len(stores) - 1:
                final += ' '
        
        return final