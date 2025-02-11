"""
firList = [[0,2],[5,10],[13,23],[24,25]]
secList = [[1,5],[8,12],[15,24],[25,26]]

Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Meeting overlaps times are inclusive

Can use a two pointer approach, since sorted, move pointer is end time is smaller than start time.
Each iteration, add overlapping times to a result array.
"""
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []

        i, j = 0, 0

        while i < len(firstList) and j < len(secondList):
            iStartTime, iEndTime = firstList[i]
            jStartTime, jEndTime = secondList[j]

            if iStartTime > jEndTime:
                j += 1
            elif jStartTime > iEndTime:
                i += 1
            else:
                result.append([max(iStartTime, jStartTime), min(iEndTime, jEndTime)])

                if iEndTime > jEndTime:
                    j += 1
                else:
                    i += 1

        return result