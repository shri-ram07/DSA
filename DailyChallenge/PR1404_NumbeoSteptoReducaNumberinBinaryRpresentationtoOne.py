class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        # Traverse from right to left, ignoring the first bit (since s[0] == '1')
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i])
            if bit + carry == 1:
                # Odd → requires +1 (carry) and then division
                steps += 2
                carry = 1
            else:
                # Even → just divide
                steps += 1
        
        # If carry remains after processing all bits, add one more step
        return steps + carry
