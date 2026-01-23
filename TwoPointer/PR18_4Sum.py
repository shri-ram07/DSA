class Solution(object):
    """
    Approach: Two Pointers inside Two More Pointers

    1. First, sort the array → makes it easier to move pointers logically and handle duplicates.
    2. Use two nested loops:
       - Outer loop picks the first number (i).
       - Inner loop picks the second number (j).
    3. After fixing i and j, use the two-pointer technique:
       - k starts just after j.
       - l starts at the end of the array.
    4. Now we have four indices (i, j, k, l) → check their sum.
       - If sum == target → store quadruplet.
       - If sum < target → move k forward (to increase sum).
       - If sum > target → move l backward (to decrease sum).
    5. Avoid duplicates by checking before adding to result.
    6. Return all unique quadruplets.
    """

    def fourSum(self, nums, target):
        # Step 1: Sort the array so we can use two-pointer logic
        nums.sort()

        # Step 2: Create a list to store the final quadruplets
        result = []

        # Step 3: Get the length of the array
        leng = len(nums)

        # Step 4: Loop for the first number (i)
        for i in range(leng - 3):  # stop at leng-3 because we need 4 numbers
            # Step 5: Loop for the second number (j)
            for j in range(i + 1, leng - 2):  # starts after i
                # Step 6: Two pointers for the remaining two numbers
                k, l = j + 1, leng - 1

                # Step 7: Move pointers until they meet
                while k < l:
                    # Step 8: Calculate the sum of four numbers
                    curr_sum = nums[i] + nums[j] + nums[k] + nums[l]

                    # Step 9: If sum matches target → valid quadruplet
                    if curr_sum == target:
                        quadruplet = [nums[i], nums[j], nums[k], nums[l]]

                        # Step 10: Add only if not already in result (to avoid duplicates)
                        if quadruplet not in result:
                            result.append(quadruplet)

                        # Step 11: Move both pointers inward
                        k += 1
                        l -= 1

                    # Step 12: If sum is smaller than target → move k forward
                    elif curr_sum < target:
                        k += 1

                    # Step 13: If sum is larger than target → move l backward
                    else:
                        l -= 1

        # Step 14: Return all unique quadruplets
        return result
