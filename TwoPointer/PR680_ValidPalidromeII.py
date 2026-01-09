class Solution(object):
    def validPalindrome(self, s):
        # Logic: Two Pointer
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # Check if the string is already a palindrome
        # If not, try removing one character from either end and check again
        # If a palindrome is found, return True, else return False
        

        # Check if the string is already a palindrome
        if s == s[::-1]:
            return True
        # If not, try removing one character from either end and check again
        else:
            # d is the number of deletions allowed
            d = 1
            # Two Pointer Approach
            l , r = 0 , len(s)-1
            # Iterate until the two pointers meet
            while l<=r:
                    # If characters at both pointers do not match
                    if s[l] != s[r] :
                        # If we have a deletion available
                        if d == 1:
                            # Try removing the left character
                            d-=1
                            # Check if the remaining string is a palindrome
                            n =  s[0:l]+s[l+1:len(s)]
                            if n[::] == n[::-1]:
                                return True
                            else:
                                r-=1
                        # If no deletions are left, return False
                        else:
                            return False
                    # If characters match, move both pointers inward
                    else:
                        l+=1
                        r-=1

            return True

obj = Solution()
a = obj.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")
print(a)

