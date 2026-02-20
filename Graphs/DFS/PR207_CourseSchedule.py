class Solution:
    def canFinish(self, numCourses, prerequisites):
        def TopologicalSort(i , ad_li , indegree):
            queue = []
            count  = 0
            for i in indegree:
                if indegree[i] == 0:
                    queue.append(i)
                    count+=1

            while queue:
                a = queue.pop(0)
                for i in ad_li[a]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        queue.append(i)
                        count+=1
            return count == numCourses
                    

        indegree = {i: 0 for i in range(numCourses)}
        # Craft a adj. List
        ad_li = {}
        for u , v in prerequisites:
            if u not in ad_li:
                ad_li[u] = []
            ad_li[u].append(v)
            indegree[v] += 1

        
        
        # print(ad_li)

        for i in range(numCourses):
            if not TopologicalSort(i , ad_li , indegree):
                return False

        
        return True
    
obj = Solution()
edges = [[1,0],[0,1]]
a = obj.canFinish(2 , edges)
print(a)