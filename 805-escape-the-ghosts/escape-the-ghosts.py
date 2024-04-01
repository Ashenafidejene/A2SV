class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        myDistance = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            ghostDistance = abs(target[0] - ghost[0]) + abs(target[1] - ghost[1])
            if ghostDistance <= myDistance:
                return False
        return True