# class Solution(object):
#     def search(self, nums, target):
#         """
#         Search in Rotated Sorted Array

#         This function searches for a target value inside a rotated sorted array.
#         A rotated sorted array is an array that was originally sorted but then
#         rotated at some pivot. For example:

#             Original sorted array: [1, 2, 3, 4, 5, 6, 7]
#             Rotated version:       [4, 5, 6, 7, 1, 2, 3]

#         The algorithm works in two phases:
#         1. Adjust the search boundaries (l, r) to find the correct sorted subspace.
#         2. Perform a standard binary search within that subspace.

#         Example:
#             nums = [4,5,6,7,0,1,2], target = 0
#             Output → 4   (index of target)

#         Diagram of rotated array:
        
#             [4, 5, 6, 7, 0, 1, 2]
#              ↑              ↑
#              l              r
             
#         After adjusting boundaries, binary search is applied:
        
#             mid = (l+r)//2
#             Compare nums[mid] with target
#             Move l or r accordingly until found or exhausted.
#         """

#         # Step 1: Initialize left and right pointers
#         l, r = 0, len(nums) - 1

#         # Step 2: Adjust boundaries if array is rotated
#         while True:
#             # If rightmost element is smaller than leftmost, array is rotated
#             if nums[r] < nums[l]:
#                 # If target is greater than nums[r], shrink right boundary
#                 if target > nums[r] and nums[r] < nums[l]:
#                     r -= 1
#                 # If target is smaller/equal to nums[r], move left boundary
#                 elif target <= nums[r] and nums[r] < nums[l]:
#                     l += 1
#             else:
#                 # Array is sorted in current subspace, break
#                 break

#         # Step 3: Standard binary search
#         while l <= r:
#             mid = (l + r) // 2  # Find middle index

#             if nums[mid] == target:
#                 return mid  # Target found
#             elif nums[mid] < target:
#                 l = mid + 1  # Search right half
#             else:
#                 r = mid - 1  # Search left half

#         # Step 4: Target not found
#         return -1
class Solution(object):
    def search(self, nums, target):
        """
        Search in Rotated Sorted Array (LeetCode 33)

        This function searches for a target value in a rotated sorted array using
        a modified binary search. The array was originally sorted in ascending order,
        but then rotated at some pivot. Example:

            Original sorted array: [0, 1, 2, 4, 5, 6, 7]
            Rotated version:       [4, 5, 6, 7, 0, 1, 2]

        🔑 Key Idea:
        - At each step, one half of the array (left or right) is guaranteed to be sorted.
        - Check if the target lies in the sorted half.
        - If yes → move into that half.
        - If no → move into the other half.
        - This ensures O(log n) time complexity.

        Example Walkthrough:
        nums = [4,5,6,7,0,1,2], target = 0

        Step 1:
        l=0, r=6, mid=3 → nums[mid]=7
        Left half [4,5,6,7] is sorted
        Target=0 not in [4..7] → search right half

        Step 2:
        l=4, r=6, mid=5 → nums[mid]=1
        Right half [0,1,2] is sorted
        Target=0 in [0..1] → search left half

        Step 3:
        l=4, r=4, mid=4 → nums[mid]=0 → FOUND

        ASCII Diagram of Search Process:

            [4, 5, 6, 7, 0, 1, 2]
             ↑           ↑     ↑
             l           mid   r

        After narrowing down:

            [0, 1, 2]
             ↑  ↑  ↑
             l mid r

        Finally:

            [0]
             ↑
             l=mid=r → target found

        Returns:
            Index of target if found, else -1
        """

        # Initialize left and right pointers
        l, r = 0, len(nums) - 1

        # Standard binary search loop
        while l <= r:
            mid = (l + r) // 2  # Middle index

            # Case 1: Target found
            if nums[mid] == target:
                return mid

            # Case 2: Left half is sorted
            if nums[l] <= nums[mid]:
                # Target lies in left half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # Case 3: Right half is sorted
            else:
                # Target lies in right half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        # Target not found
        return -1
