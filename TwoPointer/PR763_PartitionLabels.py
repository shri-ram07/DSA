class Solution(object):
    def partitionLabels(self, s):
        # we will use the three pointers 
        # i _ start of partition , end _ last element of current partition
        # j will iterate between i and end to check for another end
        # len of current partition = end - i - 1
        
        # First loop until end != len(s)
        # create hash table of the unique element for last occurances through
        # reverse Iteratation
        
        
        # Hash Table for listing all last occurence of all element
        dic = dict.fromkeys(set(s))
        for i in range(len(s)-1 , -1 , -1):
            if dic[s[i]] is None:
                dic[s[i]] = i
        #List To store the lenght of the partitions
        li = [] 
        
        #start variable
        i = 0
        # end variable will be the last occurence of the first varibale
        end = dic[s[0]]
        # Directly returning the lenght of the string if the last occurence of the first character is last 
        if end == len(s)-1:
            return [len(s)]
        
        # Iterate Until end ! len(s)
        while end != len(s)-1:
            # initialise the end varibale will be the last occurence of the first varibale
            end = dic[s[i]]
            # The j varibale which will iterate from the i to end
            j = i+1
            while j<=end:
                # Update the end varibale if last occurence if j's is greater than the end
                end = max(dic[s[j]] , end)
                #Update the j
                j+=1
            #append the list with the lenght of the partition
            li.append(end-i+1)
            #Increment the i
            i = end+1
        return li
            
            
# Implimenent of class
obj = Solution()
obj.partitionLabels("ccebabdaeddebeaeaaec")