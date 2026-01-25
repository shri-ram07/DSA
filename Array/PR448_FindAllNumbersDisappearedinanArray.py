class Solution(object):
    """
    Logic:
    We can use a set to track the numbers present in the array.
    Then, we can iterate through the range from 1 to n (where n is the length of the array)
    and check which numbers are missing from the set.
    Those missing numbers are the ones that disappeared from the array.
    Time Complexity: O(n) - We traverse the array and then the range from 1 to n.
    Space Complexity: O(n) - We use a set to store the numbers present in the array.
    """

    
    def findDisappearedNumbers(self, nums):
        # Set to track numbers present in the array
        missing_num = []
        # Length of the array
        i = len(nums)
        # Create a set of numbers present in the array
        s = set(nums)
        # Iterate from n down to 1 to find missing numbers
        while i>0:
            # Check if the number is not in the set
            if i not in s:
                # If missing, add to the result list
                missing_num.append(i)
            # Decrement i
            i-=1
        # return the missing numbers
        return missing_num