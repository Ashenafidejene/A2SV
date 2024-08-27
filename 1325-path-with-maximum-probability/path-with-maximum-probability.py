class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        
        # Build the graph
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        
        # Max-heap (priority queue), storing (-probability, node)
        max_heap = [(-1.0, start_node)]
        max_prob = [0.0] * n
        max_prob[start_node] = 1.0
        
        while max_heap:
            current_prob, node = heapq.heappop(max_heap)
            current_prob = -current_prob  # Convert back to positive
            
            # If we reached the end node, return the probability
            if node == end_node:
                return current_prob
            
            for neighbor, prob in graph[node]:
                new_prob = current_prob * prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))
        
        # If no path was found
        return 0.0