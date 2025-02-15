class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        
        stack = []
        stack.append(intervals[0])

        for i in range(1, len(intervals)):
            prevEnd = stack[-1][1]

            if prevEnd < intervals[i][0]:
                stack.append(intervals[i])
            else:
                prevStart, prevEnd = stack.pop()
                stack.append([min(prevStart, intervals[i][0]), max(prevEnd, intervals[i][1])])
        
        return stack