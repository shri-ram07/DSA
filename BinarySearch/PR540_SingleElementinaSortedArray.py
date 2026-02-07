class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        Problem:
        --------
        Given a sorted array where every element appears exactly twice except one element 
        which appears only once, find that single element in O(log n) time.

        Approach:
        ---------
        We use Binary Search to efficiently find the single element.

        Key Idea:
        - In a sorted array with pairs:
            * Before the single element → pairs start at even indices.
            * After the single element → pairs start at odd indices.
        - Using this property, we can decide whether to move left or right in the array.

        Diagram (Example):
        ------------------
        Array: [1, 1, 2, 2, 3, 4, 4, 5]
        Index:  0  1  2  3  4  5  6  7

        Step 1: l=1, r=6 → mid=3 → nums[3]=2
                nums[3] == nums[2] → valid pair → move right

        Step 2: l=4, r=6 → mid=5 → nums[5]=4
                nums[5] == nums[6] → valid pair → move left

        Step 3: l=r=4 → nums[4]=3
                nums[4] != nums[3] and nums[4] != nums[5] → unique found!

        ASCII Flow:
        -----------
        Array: [1, 1, 2, 2, 3, 4, 4, 5]
        Initial: l=1, r=6
                  ↓        ↓
        Index:    0 1 2 3 4 5 6 7
                  1 1 2 2 3 4 4 5

        Step 1: mid=3 → pair valid → move right
        Step 2: mid=5 → pair valid → move left
        Step 3: l=r=4 → nums[4]=3 → unique found!

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """

        # Define search boundaries (excluding first and last element initially)
        l , r = 1 , len(nums)-2
        
        # Edge cases:
        if len(nums) == 1:  # Only one element in array
            return nums[0]
        elif nums[0] != nums[1]:  # First element is unique
            return nums[0]
        elif nums[r] != nums[r+1]:  # Last element is unique
            return nums[r+1]
        
        # Binary search loop
        while l <= r:
            mid = (l+r)//2
            
            # Case 1: Found the unique element
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            
            # Case 2: Decide which half to search
            elif mid % 2 == 0:  # If mid is even
                if nums[mid] == nums[mid+1]:
                    # Pair is valid, so unique element must be on the right
                    l = mid+1
                else:
                    # Pair is broken, so unique element must be on the left
                    r = mid - 1
            else:  # If mid is odd
                if nums[mid] == nums[mid-1]:
                    # Pair is valid, so unique element must be on the right
                    l = mid+1
                else:
                    # Pair is broken, so unique element must be on the left
                    r = mid - 1
