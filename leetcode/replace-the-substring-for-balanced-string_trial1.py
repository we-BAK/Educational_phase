from collections import Counter
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        count = Counter(s)
        required = n // 4
        if all(count[c] == required for c in "QWER"):
            return 0
        left = 0
        min_len = n
        for right in range(n):
            count[s[right]] -= 1
            while left < n and all(count[c] <= required for c in "QWER"):
                min_len = min(min_len, right - left + 1)
                count[s[left]] += 1
                left += 1
        return min_len