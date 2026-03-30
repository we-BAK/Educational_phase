class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort()
        score = 0
        cols = len(nums[0])
        for col in range(cols - 1, -1, -1):
            max_val = 0
            for row in nums:
                max_val = max(max_val, row[col])
            score += max_val
        return score