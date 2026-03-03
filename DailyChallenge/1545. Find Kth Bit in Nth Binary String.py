class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Recursive helper
        def helper(n, k):
            if n == 1:
                return "0"
            
            length = (1 << n) - 1   # 2^n - 1
            mid = (length // 2) + 1
            
            if k == mid:
                return "1"
            elif k < mid:
                return helper(n - 1, k)
            else:
                # Mirror position in left half
                mirrored = mid - (k - mid)
                bit = helper(n - 1, mirrored)
                return "1" if bit == "0" else "0"
        
        return helper(n, k)

        
