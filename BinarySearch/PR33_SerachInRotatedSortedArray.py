class Solution(object):
    def search(self, nums, target):
        """
        Search in Rotated Sorted Array

        This function searches for a target value inside a rotated sorted array.
        A rotated sorted array is an array that was originally sorted but then
        rotated at some pivot. For example:

            Original sorted array: [1, 2, 3, 4, 5, 6, 7]
            Rotated version:       [4, 5, 6, 7, 1, 2, 3]

        The algorithm works in two phases:
        1. Adjust the search boundaries (l, r) to find the correct sorted subspace.
        2. Perform a standard binary search within that subspace.

        Example:
            nums = [4,5,6,7,0,1,2], target = 0
            Output → 4   (index of target)

        Diagram of rotated array:
        
            [4, 5, 6, 7, 0, 1, 2]
             ↑              ↑
             l              r
             
        After adjusting boundaries, binary search is applied:
        
            mid = (l+r)//2
            Compare nums[mid] with target
            Move l or r accordingly until found or exhausted.
        """

        # Step 1: Initialize left and right pointers
        l, r = 0, len(nums) - 1

        # Step 2: Adjust boundaries if array is rotated
        while True:
            # If rightmost element is smaller than leftmost, array is rotated
            if nums[r] < nums[l]:
                # If target is greater than nums[r], shrink right boundary
                if target > nums[r] and nums[r] < nums[l]:
                    r -= 1
                # If target is smaller/equal to nums[r], move left boundary
                elif target <= nums[r] and nums[r] < nums[l]:
                    l += 1
            else:
                # Array is sorted in current subspace, break
                break

        # Step 3: Standard binary search
        while l <= r:
            mid = (l + r) // 2  # Find middle index

            if nums[mid] == target:
                return mid  # Target found
            elif nums[mid] < target:
                l = mid + 1  # Search right half
            else:
                r = mid - 1  # Search left half

        # Step 4: Target not found
        return -1
