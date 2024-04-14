class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        answer = 0 
        k = len(tasks)-1
        for i in range(len(processorTime)):
            answer = max (answer,tasks[k]+processorTime[i])
            k-=4
        return answer 
