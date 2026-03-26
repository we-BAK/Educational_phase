class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
        max_len = 1
        curr = 1
        for i in range(1, n):
            if arr[i] == arr[i-1]:
                curr = 1
            elif i == 1 or (arr[i] - arr[i-1]) * (arr[i-1] - arr[i-2]) >= 0:
                curr = 2
            else:
                curr += 1
            max_len = max(max_len, curr)
        return max_len