from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        """
        Calculate the minimum cost by taking the first element
        and adding the two smallest values from the rest of the list.
        """

        # Start with the first element as the initial score
        score = nums[0]

        # Get the remaining elements (excluding the first one)
        arr = nums[1:]

        # Sort the remaining elements to easily find the smallest ones
        arr.sort()

        # Add the sum of the two smallest elements to the score
        score += sum(arr[0:2])

        # Return the final minimum cost
        return score
