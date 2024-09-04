class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans = [0, 0]  # Robot's current position
        dir = 0  # Current direction (0: north, 1: east, 2: south, 3: west)
        priv = 0  # Previous direction to revert if hitting an obstacle
        
        # Convert list of lists to a set of tuples for fast lookup
        obs = set(map(tuple, obstacles))
    
        maxs = 0 
        for arrow in commands:
            if arrow == -1:  # Turn right
                priv = dir 
                dir = (dir + 1) % 4
                continue
            if arrow == -2:  # Turn left
                priv = dir 
                dir = (dir - 1) % 4
                continue
            
            # Moving in the current direction
            if dir == 0:  # North
                for _ in range(arrow):
                    ans[1] += 1
                    if tuple(ans) in obs:
                        ans[1] -= 1
                        break
            elif dir == 1:  # East
                for _ in range(arrow):
                    ans[0] += 1
                    if tuple(ans) in obs:
                        ans[0] -= 1
                        break
            elif dir == 2:  # South
                for _ in range(arrow):
                    ans[1] -= 1
                    if tuple(ans) in obs:
                        ans[1] += 1
                        
                        break
            else:  # West
                for _ in range(arrow):
                    ans[0] -= 1
                    if tuple(ans) in obs:
                        ans[0] += 1
                        break
            
            # Update the maximum distance squared
            maxs = max(maxs, (ans[0] * ans[0] + ans[1] * ans[1]))
        
        return maxs
            