def minimum_swaps(arr):
    """
    Calculates the minimum number of swaps to sort an array.
    
    This implementation uses the cycle decomposition method. Any permutation 
    can be decomposed into disjoint cycles. For a cycle of size 'k', 
    the number of swaps required to sort it is 'k - 1'.

    Big O Complexity:
        Time: O(n log n) due to the sorting of enumerations.
        Space: O(n) to store the visited nodes and sorted pairs.

    Arg:
        arr (list): A list of n elements.

    Return:
        int: The minimum number of swaps required.
    """
    n = len(arr)
    # Create pairs of (index, value) and sort them by value. This handles any data type and identifies where each element should be
    sorted_pairs = sorted(enumerate(arr), key=lambda x: x[1])
    
    visited = [False] * n
    swaps = 0

    for i in range(n):
        # If element is already visited or already in the correct position
        if visited[i] or sorted_pairs[i][0] == i:
            continue

        # Find the size of the cycle
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            # Move to the original index of the element currently at sorted_pairs[j]
            j = sorted_pairs[j][0]
            cycle_size += 1

        # A cycle of size k requires (k - 1) swaps
        if cycle_size > 1:
            swaps += (cycle_size - 1)

    return swaps