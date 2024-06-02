class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        link = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        for a, b in prerequisites:
            link[a].append(b)


        def recursive(n):
            if visited[n] == 1: # 방문 중이면 loop
                return False
            if visited[n] == 2: # 이미 탐색한 nei
                return True

            visited[n] = 1 # 방문 중
            for nei in link[n]:
                if not recursive(nei):
                    return False
            visited[n] = 2 # 방문 완료
            return True

        for i in range(numCourses):
            if not recursive(i):
                return False

        return True