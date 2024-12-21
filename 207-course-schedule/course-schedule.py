class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i : [] for i in range(numCourses)}
        visited = set()

        for crs, pre in prerequisites:
            courses[crs].append(pre)
        
        def dfs(crs):
            if crs in visited:
                return False
            
            if courses[crs] == []:
                return True
            
            visited.add(crs)

            for c in courses[crs]:
                if not dfs(c):
                    return False
                
            visited.remove(crs)
            courses[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

            

