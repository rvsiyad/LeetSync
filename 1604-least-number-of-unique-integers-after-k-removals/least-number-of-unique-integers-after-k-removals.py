class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)

        sorted_items = sorted(count.items(), key=lambda x: x[1])

        for key, freq in sorted_items:
            if k >= freq:
                k -= freq
                del count[key]
            else:
                break
        
        return len(count)