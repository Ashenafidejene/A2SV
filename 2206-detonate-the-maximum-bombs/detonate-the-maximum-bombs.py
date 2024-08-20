class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = {i : [] for i in range( len(bombs))}
        for i in range (len(bombs)):
            for j in range(i+1,len(bombs)):
                x1,y1,r1 = bombs[i]
                x2,y2,r2 = bombs[j]
                d = sqrt((x1-x2)**2 + (y1-y2)**2)
                if d <= r1 :
                    graph[i].append(j)
                if d <= r2 :
                    graph[j].append(i)
        
        def dfs(i , visit):
            if i in visit :
                return 0 
            visit.add(i)
            count = 1
            for nigbour in graph[i]:
                if nigbour not in  visit:
                    count += dfs(nigbour,visit)
            return count 
        res =  0 
        for i in range(len(bombs)):
            res = max(res,dfs(i,set()))
        return res 

                    

