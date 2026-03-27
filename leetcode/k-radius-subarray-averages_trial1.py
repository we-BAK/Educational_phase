class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        window_size = 2 * k + 1
        if window_size > n:
            return res
        
        window_sum = 0
        for i in range(window_size):
            window_sum += nums[i]
    
        res[k] = window_sum // window_size
        
        for i in range(window_size, n):
            window_sum += nums[i]                 
            window_sum -= nums[i - window_size]    
            
            center = i - k
            res[center] = window_sum // window_size
        
        return res