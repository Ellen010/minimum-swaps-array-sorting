# Minimum Swaps to Sort an Array

This project implements a Python algorithm that calculates the **minimum number of swaps required to sort an array of unique integers in ascending order**.

The solution works by detecting **cycles in the permutation of elements**.
For each cycle of length `k`, only `k - 1` swaps are required to place all elements in their correct positions.

## Algorithm Overview

1. Sort the array to determine the correct position of each value.
2. Build a mapping from value → correct index.
3. Traverse the array and detect cycles using a `visited` tracker.
4. For each cycle, add `cycle_size - 1` to the total number of swaps.

## Time & Space Complexity

* **Time Complexity:** `O(n log n)` (due to sorting)
* **Space Complexity:** `O(n)`

## Example

```python
arr = [4, 3, 1, 2]
print(minimum_swaps(arr))
```

Output:

```
3
```

## Use Case

This algorithm is commonly used in **coding interviews and algorithmic problem solving**, particularly when optimizing sorting operations with minimal swaps.
