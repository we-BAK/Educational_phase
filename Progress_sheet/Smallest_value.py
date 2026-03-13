class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        
        if num > 0:
            digits = sorted(str(num))
            
            if digits[0] == '0':
                for i in range(len(digits)):
                    if digits[i] != '0':
                        digits[0], digits[i] = digits[i], digits[0]
                        break
            
            return int("".join(digits))
        
        else:
            digits = sorted(str(-num), reverse=True)
            return -int("".join(digits))
        