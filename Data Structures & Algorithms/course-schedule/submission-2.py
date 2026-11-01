class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        verified = set()

        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        self.currPath = set()

        def dfs(crs):
            if crs in verified:
                return True

            if crs in self.currPath:
                return False
            
            self.currPath.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            self.currPath.remove(crs)
            verified.add(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

