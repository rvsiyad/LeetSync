'''
 - Use hashmap to keep counts
 - We check at each index if value A is in B and value B in A.
 - Keep a running count
'''

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        count = 0
        result = []
        a_set = set()
        b_set = set()

        for i in range(len(A)):
            a_set.add(A[i])
            b_set.add(B[i])

            if A[i] == B[i]:
                count += 1
                result.append(count)
                continue

            if A[i] in b_set:
                count += 1
            
            if B[i] in a_set:
                count += 1
            
            result.append(count)
        
        return result