def sortByBits(arr):
    """
    Sorts a list of integers based on the number of '1' bits in their binary representation.
    
    Primary key: Count of '1's in binary form (ascending).
    Secondary key: Numerical value itself (ascending, used when counts tie).
    
    Example:
        Input:  [0,1,2,3,4,5,6,7,8]
        Output: [0,1,2,4,8,3,5,6,7]
        
    Explanation:
        - 0 -> binary '0'  -> 0 ones
        - 1 -> binary '1'  -> 1 one
        - 2 -> binary '10' -> 1 one
        - 3 -> binary '11' -> 2 ones
        - 4 -> binary '100'-> 1 one
        - 5 -> binary '101'-> 2 ones
        - 6 -> binary '110'-> 2 ones
        - 7 -> binary '111'-> 3 ones
        - 8 -> binary '1000'-> 1 one
        Sorted first by count of ones, then by numeric value.
    """
    
    # Use Python's built-in sorted() with a custom key
    # The key is a tuple: (bit_count, number)
    # - bit_count ensures numbers are grouped by how many '1's they have
    # - number ensures ties are broken by ascending numeric order
    
    return sorted(arr, key=lambda x: (x.bit_count(), x))
