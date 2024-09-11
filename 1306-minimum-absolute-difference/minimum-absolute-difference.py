class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        dic = {}
        minDiff = float("inf")
        arr.sort()

        L = 0

        for R in range(1, len(arr)):
            currDiff = abs(arr[R] - arr[L])
            minDiff = min(currDiff, minDiff)

            if currDiff in dic:
                dic[currDiff].append([arr[L], arr[R]])

            else:
                dic[currDiff] = [[arr[L], arr[R]]]
            
            L += 1
        return dic[minDiff]