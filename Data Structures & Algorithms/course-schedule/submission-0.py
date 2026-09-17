class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency_list = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        for course,prereq in prerequisites:
            adjacency_list[prereq].append(course)
            indegrees[course] +=1
        queue = []
        print(indegrees)
        
        for num,degree in enumerate(indegrees):
            if 0 == degree:
                queue.append(num)

        if not queue:
            return False
        
        courses_taken = 0
        print(adjacency_list)
        
        while queue:
            current = queue.pop()
            print(current)
            courses_taken +=1
            neighbors = adjacency_list[current]
            print(neighbors)

            for n in neighbors:
                indegrees[n] -=1
                if indegrees[n] == 0:
                    print(0)
                    queue.append(n)
        return courses_taken == numCourses
        