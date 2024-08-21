class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = {i: [] for i in range(n)}
        
        
        for parent, child in edges:
            graph[parent].append(child)
            graph[child].append(parent)
        
        ans = [0] * n
        
        def dfs(node, parent):
            count = defaultdict(int)
            count[labels[node]] += 1
            
            for neighbor in graph[node]:
                if neighbor != parent:  
                    child_count = dfs(neighbor, node)
                    for label, freq in child_count.items():
                        count[label] += freq
            
            ans[node] = count[labels[node]]
            return count
        
        dfs(0, -1)
        return ans
