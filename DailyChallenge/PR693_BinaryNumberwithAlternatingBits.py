class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Step 1: Convert number to binary string
        # bin(n) gives '0b...' format, so str(bin(n)) = '0b101...'
        binary = str(bin(n))
        
        # Step 2: Loop through binary string starting from index 1
        # Compare each bit with the previous one
        for x in range(1, len(binary)):
            # If two consecutive bits are same → not alternating
            if binary[x] == binary[x-1]:
                return False
        
        # Step 3: If loop finishes without finding same consecutive bits
        # → number has alternating bits
        return True
