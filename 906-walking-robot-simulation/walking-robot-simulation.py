class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans = [0, 0]  
        dir = 0  
        
        
        obs = set(map(tuple, obstacles))
    
        maxs = 0 
        for arrow in commands:
            if arrow == -1:  
                priv = dir 
                dir = (dir + 1) % 4
                continue
            if arrow == -2:  
                priv = dir 
                dir = (dir - 1) % 4
                continue
            
            if dir == 0:  
                for _ in range(arrow):
                    ans[1] += 1
                    if tuple(ans) in obs:
                        ans[1] -= 1
                        break
            elif dir == 1: 
                for _ in range(arrow):
                    ans[0] += 1
                    if tuple(ans) in obs:
                        ans[0] -= 1
                        break
            elif dir == 2:  
                for _ in range(arrow):
                    ans[1] -= 1
                    if tuple(ans) in obs:
                        ans[1] += 1
                        break
            else:  
                for _ in range(arrow):
                    ans[0] -= 1
                    if tuple(ans) in obs:
                        ans[0] += 1
                        break
            
            maxs = max(maxs, (ans[0] * ans[0] + ans[1] * ans[1]))
        
        return maxs
            