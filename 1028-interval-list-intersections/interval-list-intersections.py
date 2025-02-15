class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        l1, l2 = 0, 0

        result = []

        while l1 < len(firstList) and l2 < len(secondList):
            firstStart, firstEnd = firstList[l1]
            secondStart, secondEnd = secondList[l2]

            if firstEnd >= secondStart and secondEnd >= firstStart:
                result.append([max(firstStart, secondStart), min(firstEnd, secondEnd)])

                if firstEnd > secondEnd:
                    l2 += 1
                else:
                    l1 += 1
            elif firstEnd > secondEnd:
                l2 += 1
            else:
                l1 += 1
        
        return result
