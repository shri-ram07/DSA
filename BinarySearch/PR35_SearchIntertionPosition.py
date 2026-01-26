class Solution(object):
    def searchInsert(self, nums, target):
        """
        Find the index at which the target should be inserted in a sorted list.

        This method uses binary search to:
        - Return the index if the target is found in the list.
        - Return the index where the target should be inserted to maintain sorted order.

        Args:
            nums (List[int]): A sorted list of integers (ascending order).
            target (int): The integer value to search for.

        Returns:
            int: The index of the target if found, or the index where it should be inserted.
        """

        # Initialize left and right pointers
        l, r = 0, len(nums) - 1

        # Binary search loop
        while l <= r:
            mid = (l + r) // 2  # Middle index

            if nums[mid] == target:
                # Target found at mid index
                return mid
            elif nums[mid] < target:
                # Target lies in the right half
                l = mid + 1
            else:
                # Target lies in the left half
                r = mid - 1

        # If target not found, l will be the correct insert position
        return l
