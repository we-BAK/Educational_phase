class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_sub=sum(nums[:k])
        max_sub=sum_sub
        for i in range(k,len(nums)):
            sum_sub+=nums[i]-nums[i-k]
            max_sub=max(max_sub,sum_sub)
        return max_sub/k


