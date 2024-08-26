class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic = {}
        minHeap = []

        for i in points:
            x = i[0]
            y = i[1]

            eucDis = math.sqrt((x ** 2) + (y ** 2))

            minHeap.append(eucDis)

            if eucDis in dic:
                arr = dic[eucDis]
                arr.append(i)
                dic[eucDis] = arr
            else:
                dic[eucDis] = [i]
            
        
        # print(dic)

        heapq.heapify(minHeap)

        res = []

        while k > 0:
            value = heapq.heappop(minHeap)
            matching = dic[value]

            if len(matching) > 1:
                res.append(matching.pop())
            else:
                res.append(matching.pop())
            
            k -= 1
        
        print(res)
        return res
