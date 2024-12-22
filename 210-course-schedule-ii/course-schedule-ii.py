class Solution:
    """
    1. First step we should take is to create an adj list for courses numbered from 0 - numCourses - 1
    2. Add courses to adjList by populating with the prereqs - adjList[crs].append(pre)
    3. Create a visited set() if we encounter a cycle, we know there is a loop, impossible to finish all courses.
    4. Now we can DFS through the courses, if we find a course with no prereqs, then we can add to results array.
    5. If we encounter a visited course, return empty array.
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i : [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        visited, inRes = set(), set()
        result = []

        # We can loop through all courses?
        # Create a DFS func?
        # We can clear the courses once we know we can reach them? 
        def dfs(crs):
            if crs in visited or crs not in adjList:
                return False
            
            if adjList[crs] == []:
                if crs not in inRes:
                    result.append(crs)
                    inRes.add(crs)
                
                return True
            
            visited.add(crs)

            for pre in adjList[crs]:
                if not dfs(pre):
                    return False
            
            visited.remove(crs)
            if crs not in inRes:
                inRes.add(crs)
                result.append(crs)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return result
            


