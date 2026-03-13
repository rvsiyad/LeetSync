'''
 We go through each layer, count the number of cameras
 - We can just count number of 1's, then we can times by next cameras greater than 0
 - keep a running result
'''

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        prev_count = 0

        for col in bank[0]:
            if col == "1":
                prev_count += 1
        

        for i in range(1, len(bank)):
            bank_level = bank[i]
            curr_count = 0

            for col in bank_level:
                if col == "1":
                    curr_count += 1
            
            if curr_count == 0:
                continue
            
            result += prev_count * curr_count
            prev_count = curr_count


        return result