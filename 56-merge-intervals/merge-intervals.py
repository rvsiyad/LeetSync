class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        arr = []

        for i in range(len(intervals)):
            if arr:
                start, end = intervals[i]
                prevStart, prevEnd = arr[-1]

                print(prevStart)

                if prevEnd >= start:
                    arr.pop()
                    arr.append([min(start, prevStart), max(prevEnd, end)])
                else:
                    arr.append(intervals[i])
            
            else:
                arr.append(intervals[i])

        return arr
