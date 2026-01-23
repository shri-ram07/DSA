class Solution(object):
    def findSubstring(self, s, words):
        """
        Logic : Use sliding window
        - Create a map to store the count of each word in words list
        - Iterate through the string s with a window size equal to the total length of first words
        - We will move the window one by one untill found a occurance of any one words
        - When found we will check for next words by moving the window of size equal to length of one word
        - We will maintain a current map to track the count of words found in current window
        - If we found all words in current window then we will add the start index to result

        - Time Complexity : O(N * M) where N is length of string s and M is number of words
        - Space Complexity : O(M) for storing the word map

        - When cnt equals to length of words then we found all words in current window
        - We will reset the current map to original word map for next iteration and add the start index to results
        - Finally return the results list
        """

        # Create a map to store the count of each word in words list
        wordMap = {}
        # current map to track the count of words found in current window
        current_map = {}
        # Populate the word map and current map
        for x in words:
            if x not in wordMap:
                wordMap[x] = 1
                current_map[x] = 1
            else:
                wordMap[x] += 1
                current_map[x] += 1
        # List to store the results
        results = []
        # Length of one word
        k = len(words[0])
        # Iterate through the string s with a window size equal to the total length of first words
        for x in range(0, len(s) - k * len(words) + 1):
            # Set the left and right pointers for the window
            l, r = x, x + k
            # Initialize the start index and current substring
            start = l
            # current sub string
            st = s[l:r]
            # cnt to store count of words found in current window
            cnt = 0
            # Move the window one by one untill found a occurance of any one words
            a, b = l, r
            # Check for next words by moving the window of size equal to length of one word
            while st in wordMap and current_map[st] != 0:
                # If found we will decrease the count of that word in current map
                current_map[st] -= 1
                # Increase the count of words found in current window
                cnt += 1
                # Move the window
                a += k
                # Update the b pointer
                b += k
                # Update the current substring
                st = s[a:b]
                # Update the right pointer
            # If we found all words in current window then we will add the start index to result
            else:
                #  Check if all words are found
                if cnt == len(words):
                    # Add the start index to results
                    results.append(start)
                # Reset the cnt
                    cnt = 0
                # Reset the  current map to original word map for next iteration
                current_map = wordMap.copy()
        # Finally return the results list
        return results

          
        
        
o = Solution()
a = o.findSubstring("wordgoodgoodgoodbestword" ,["word","good","best","good"])
print(a)