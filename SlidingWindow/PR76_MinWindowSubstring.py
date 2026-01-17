class Solution(object):
    def minWindow(self, s, t):
        # We will use sliding window approach and track of window by r and l
        # variable storing right and left Pointer
        # We will use min_win for storing minimum window and start_idx for storing
        # Starting Index of the min window
        
        # Firstly we will create HAsh Map of t to track the char counts
        # Count varibale will store the count of the variable required
        # to be matched or it should be equal to len(t)
        
        # We will move r pointer in s , check if the varible is in map
        # if yes then decrease the count var and move on untill get count 0
        # If got count zero then we will check for the shrink , How much we can shrink 
        # the window by moving l pointer Untill get count>0
        # We will keep track of min_win , if found then update the start_idx
        
        # Two Pointer for window widhth
        l , r = 0 , 0 
        # min_win for minimum window and start_idx for starting index of min_win
        # we will initialize min_win with len(s) ---> Maximum possible
        min_win = float("inf")
        start_idx = 0
        # create HashMap of the t
        MAP = {}
        for x in range(len(t)):
            if t[x] not in MAP:
                MAP[t[x]] = 1
            else:
                MAP[t[x]]+=1
        # cnt for counter var
        cnt = len(t)
        # Start the loop untill r<len(s)
        while r<len(s):
            # I'll start with the first element and check if it is in MAP if not then I'll continue and 
            # if yes then Decrement the value of s[r] and decrement the value of cnt is the element in map
            # has value greater than 0
            if s[r] in MAP:
                if MAP[s[r]]>0:
                    cnt-=1 
                MAP[s[r]]-=1
            # loop this untill cnt == 0 to shrink the window to minimun size
            while cnt == 0:
                # if the current  win len is smaller than the min_win then update the min_win and start_idx
                if r - l + 1 < min_win:
                    min_win = r - l + 1
                    start_idx = l
                # if the lTH element is in MAP then increament it , and if after increament 
                # the value get positive then increment the cnt
                if s[l] in MAP:
                    MAP[s[l]]+=1
                    if MAP[s[l]]>0:
                        cnt+=1
                #Increse the l 
                l+=1
            # increase the r
            r+=1
        
        return "" if min_win == float("inf") else s[start_idx:start_idx+min_win]