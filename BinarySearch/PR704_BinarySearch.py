class Solution(object):
    """Binary search implementation
    Logic: Use two pointers to narrow down the search space.
    Time Complexity: O(log n) - Each step reduces the search space by half.
    Space Complexity: O(1) - No additional space is used.
    """
    def search(self, nums, target):
        # Initialize left and right pointers
        l , r = 0 , len(nums)-1
        # Perform binary search
        while l<=r:
            # Calculate mid index
            mid = (l+r)//2
            # Check if mid element is the target
            if nums[mid] == target:
                # Return the index of the target element
                return mid
            # Adjust search space based on comparison
            elif nums[mid] < target:
                # Move left pointer to mid + 1
                l = mid+1
            # Move right pointer to mid - 1
            else:
                # Move right pointer to mid - 1
                r = mid-1
        # Target not found, return -1
        return -1