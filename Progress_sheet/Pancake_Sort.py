class Solution:
    def pancakeSort(self, arr):
        result = []
        n = len(arr)
        for size in range(n, 1, -1):
            max_index = arr.index(size)
            
            if max_index != size - 1:
                if max_index != 0:
                    result.append(max_index + 1)
                    arr[:max_index+1] = reversed(arr[:max_index+1])
                result.append(size)
                arr[:size] = reversed(arr[:size])
        return result