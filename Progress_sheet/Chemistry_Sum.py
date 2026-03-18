class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        
        total_sum = sum(skill)
        teams = n // 2
       
        if total_sum % teams != 0:
            return -1
        
        target = total_sum // teams
        
        left = 0
        right = n - 1
        chemistry_sum = 0
        
        while left < right:
            if skill[left] + skill[right] != target:
                return -1
            
            chemistry_sum += skill[left] * skill[right]
            left += 1
            right -= 1
        
        return chemistry_sum