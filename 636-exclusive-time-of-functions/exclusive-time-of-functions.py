class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # We can use a stack to keep track of the call stacks
        executionTimes = [0] * n
        previousStartTime = 0

        stack = []

        for log in logs:
            funcId, startOrEnd, timeStamp = log.split(':')

            funcId = int(funcId)
            timeStamp = int(timeStamp)

            if startOrEnd == "start":
                # Calculate the running time for the previous, use the prev start and end of current
                # Update the execution times
                if stack:
                    executionTimes[stack[-1]] += timeStamp - previousStartTime
                
                stack.append(funcId)
                previousStartTime = timeStamp
            else:
                executionTimes[stack.pop()] += timeStamp - previousStartTime + 1
                previousStartTime = timeStamp + 1
        
        return executionTimes

