class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        components = n
        
        for u,v in edges:
            parent_u = find(u)
            parent_v = find(v)
            if parent_u != parent_v:
                parent[parent_v] = parent_u
                components -=1
        return components
        