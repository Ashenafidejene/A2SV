class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_queue = deque()
        max_queue = deque()
        start = 0
        max_size = 0

        for end in range(len(nums)):
            while min_queue and nums[end] < min_queue[-1]:
                min_queue.pop()
            min_queue.append(nums[end])

            while max_queue and nums[end] > max_queue[-1]:
                max_queue.pop()
            max_queue.append(nums[end])

            if max_queue[0] - min_queue[0] > limit:
                if max_queue[0] == nums[start]:
                    max_queue.popleft()
                if min_queue[0] == nums[start]:
                    min_queue.popleft()
                start += 1

            max_size = max(max_size, end - start + 1)

        return max_size