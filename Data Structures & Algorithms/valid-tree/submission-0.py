class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adj = {i:[] for i in range(n)}

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        queue = deque([(0, -1)])
        seen = {0}
    
        while queue:
            node, parent = queue.popleft()
        
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue  # Skip the edge back to parent
                if neighbor in seen:
                    return False  # Cycle detected
            
                seen.add(neighbor)
                queue.append((neighbor, node))
            
    # Check if all n nodes were reached
        return len(seen) == n