class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Remove underscores and compare - the relative order of L and R must be same
        if start.replace('_', '') != target.replace('_', ''):
            return False
        
        n = len(start)
        j = 0
        
        for i in range(n):
            if start[i] == '_':
                continue
            # Find the matching character in target
            while j < n and target[j] == '_':
                j += 1
            
            # L can only move left, so start index should be >= target index
            if start[i] == 'L' and i < j:
                return False
            # R can only move right, so start index should be <= target index
            if start[i] == 'R' and i > j:
                return False
            j += 1
        
        return True