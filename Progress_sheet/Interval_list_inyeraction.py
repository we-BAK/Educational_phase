class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []

        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]
            start = max(a_start, b_start)
            end = min(a_end, b_end)
            if start <= end:
                result.append([start, end])
            if a_end < b_end:
                i += 1
            else:
                j += 1
        return result
        