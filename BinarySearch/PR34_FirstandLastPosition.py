class Solution(object):
    def searchRange(self, nums, target):
        """
        Intuition:
        -----------
        We want to find the FIRST and LAST position of a target in a sorted array.
        Think of it like shining a flashlight from the LEFT side to catch the first
        occurrence, and then shining from the RIGHT side to catch the last occurrence.

        Diagram:
        --------
        Example: nums = [5,7,7,8,8,10], target = 8

        Index:   0   1   2   3   4   5
        Value:   5   7   7   8   8   10
                          ^       ^
                          |       |
                        First    Last

        We use binary search TWICE:
        - First binary search: find the left boundary (first occurrence).
        - Second binary search: find the right boundary (last occurrence).

        Why binary search?
        ------------------
        Because the array is sorted, binary search lets us "zoom in" quickly
        instead of scanning linearly.

        Pattern to remember:
        --------------------
        - Left search: shrink towards left until you can't anymore.
        - Right search: shrink towards right until you can't anymore.
        """

        i, j = 0, len(nums) - 1
        li = []

        # Edge case: empty array
        if len(nums) == 0:
            return [-1, -1]

        # -------------------------------
        # First binary search: find LEFT boundary
        # -------------------------------
        while i <= j:
            mid = (i + j) // 2

            # If target is at very first index
            if nums[0] == target:
                mid = 0
                break

            # Found target AND previous element is different → first occurrence
            if nums[mid] == target and nums[mid - 1] != target:
                break
            else:
                # If target found but previous is same → move left
                if nums[mid] == target and nums[mid - 1] == target:
                    j = mid - 1
                # If mid value is bigger than target → move left
                elif nums[mid] > target:
                    j = mid - 1
                # Otherwise move right
                else:
                    i = mid + 1

        # If we found target, store first position
        if nums[mid] == target:
            li.append(mid)

        # -------------------------------
        # Second binary search: find RIGHT boundary
        # -------------------------------
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2

            # If target is at very last index
            if nums[len(nums) - 1] == target:
                mid = len(nums) - 1
                break

            # Found target AND next element is different → last occurrence
            if nums[mid] == target and nums[mid + 1] != target:
                break
            else:
                # If target found but next is same → move right
                if nums[mid] == target and nums[mid + 1] == target:
                    i = mid + 1
                # If mid value is bigger than target → move left
                elif nums[mid] > target:
                    j = mid - 1
                # Otherwise move right
                else:
                    i = mid + 1

        # If we found target, store last position
        if nums[mid] == target:
            li.append(mid)

        # Return result: [first, last] or [-1, -1] if not found
        return li if li else [-1, -1]
