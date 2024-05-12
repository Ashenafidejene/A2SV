class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for checker in logs : 
            if checker == "../" and len(stack) != 0:
                stack.pop()
            elif checker == "../" or checker == "./":
                continue
            else:
                stack.append(checker)
        return len(stack)
