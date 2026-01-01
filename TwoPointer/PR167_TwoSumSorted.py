class Solution(object):
    # I used Two Pointer Approach
    # from two different ends due to its 
    # Sorted nature and I Used Binary
    # Search Logic to reduce the search space.

    # [Time Complexity]: O(N)
    # [Space Complexity]: O(1)

    # [0 , 1 , 2 , 3 , 4  , 9 , 56 , 90]
    # |                               |
    # l                               r
    def twoSum(self, numbers, target):
        r , l= len(numbers) - 1 , 0
        while True:
            sum =numbers[r]+numbers[l]
            if sum == target:
                # I incremented by 1 because the
                # question required 1-based indexing.
                return [l+1 , r+1]
            elif sum < target:
                l+=1
            elif sum > target:
                r-=1