class Solution(object):
    def search(self, nums, target):
        """
        Search in Rotated Sorted Array II (LeetCode 81)

        ------------------------------------------------------------
        Problem:
        Given an array `nums` that is sorted in ascending order and 
        then rotated at some pivot (unknown), possibly containing 
        duplicates, determine if `target` exists in the array.

        Example:
        nums = [2,5,6,0,0,1,2], target = 0  → True
        nums = [2,5,6,0,0,1,2], target = 3  → False

        ------------------------------------------------------------
        Approach:
        This solution uses a modified **binary search**:
        1. Compute mid index.
        2. If nums[mid] == target → found.
        3. Handle duplicates:
           - If nums[mid] == nums[l] → increment l (skip duplicate).
           - If nums[mid] == nums[r] → decrement r (skip duplicate).
        4. Determine which half is sorted:
           - If left half [l..mid] is sorted:
                → check if target lies in [l..mid-1].
           - Else right half [mid..r] is sorted:
                → check if target lies in [mid+1..r].
        5. Adjust l and r accordingly.
        6. Repeat until l > r.

        ------------------------------------------------------------
        Time Complexity:
        - Best/Average: O(log n) (binary search behavior)
        - Worst Case: O(n) (when duplicates force linear shrinking)

        Space Complexity:
        - O(1) (constant extra space)

        ------------------------------------------------------------
        ASCII Diagram of Rotated Array:
        
        Suppose nums = [4,5,6,7,0,1,2]
        
        Original sorted array: [0,1,2,4,5,6,7]
        Rotated at pivot = 3:
        
        Index:   0  1  2  3  4  5  6
        nums:   [4, 5, 6, 7, 0, 1, 2]
        
        Target = 0
        - mid = 3 → nums[mid] = 7
        - Left half [4,5,6,7] is sorted
        - Target not in left half → search right half [0,1,2]
        - Found target at index 4

        ------------------------------------------------------------
        Edge Cases Covered:
        - Empty array → returns False
        - Single element array → works correctly
        - All elements same as target → returns True
        - All elements same but not target → returns False
        - Array with heavy duplicates → still correct, but O(n)

        ------------------------------------------------------------
        Returns:
        True if target exists in nums, otherwise False.
        """

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            # Case 1: Found target
            if nums[mid] == target:
                return True

            # Case 2: Skip duplicates on left
            if nums[mid] == nums[l]:
                l += 1
                continue

            # Case 3: Skip duplicates on right
            if nums[mid] == nums[r]:
                r -= 1
                continue

            # Case 4: Left half is sorted
            elif nums[mid] > nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # target lies in left half
                else:
                    l = mid + 1  # target lies in right half

            # Case 5: Right half is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # target lies in right half
                else:
                    r = mid - 1  # target lies in left half

        # Target not found
        return False
