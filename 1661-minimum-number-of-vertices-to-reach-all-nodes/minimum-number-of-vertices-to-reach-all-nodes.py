
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = set()
        for src, dst in edges:
            incoming.add(dst)
        res = []
        for i in range(n):
            if i not in incoming:
                res.append(i)
        return res