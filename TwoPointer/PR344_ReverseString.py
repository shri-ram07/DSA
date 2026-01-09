class Solution(object):
    def reverseString(self, s):
        # Logic: Two Pointer
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # Two Pointer Approach
        # Loop through the first half of the string
        # Swap the characters at the left and right pointers
        # Move the right pointer towards the center


        # Initialize right pointer
        r = len(s)-1
        # Iterate through the first half of the string
        for l in range(0 , len(s)//2):
            # Swap characters at left and right pointers
            s[l] , s[r] = s[r] , s[l]
            # Move right pointer towards the center
            r-=1
        # return the reversed string
        return s
obj = Solution()
a = obj.reverseString(["h","e","l","l","o"])
print(a)