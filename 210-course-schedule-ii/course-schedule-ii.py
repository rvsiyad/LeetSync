class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Similar to CS-1, but this time we add to the results array each time we find a course than has been completed. Create a seperate set to see if in the courses completed array, if not in add else continue.
        crsToPre = {i : [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            crsToPre[crs].append(pre)
        
        visited = set()
        inResult = set()
        result = []

        def dfs(course):
            if course in visited or course not in crsToPre:
                return False
            
            if crsToPre[course] == []:
                if course not in inResult:
                    result.append(course)
                    inResult.add(course)
                return True
            
            visited.add(course)

            for pre in crsToPre[course]:
                if not dfs(pre):
                    return False
            
            visited.remove(course)

            if course not in inResult:
                result.append(course)
                inResult.add(course)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return result