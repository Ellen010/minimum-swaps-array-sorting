# Minimum Swaps to Sort an Array

This project provides an efficient Python implementation to calculate the **minimum number of swaps required to sort an array**.

The solution is based on **Cycle Decomposition Theory**, which treats the array as a directed graph where an edge exists from the current index to the index where the element *should* be.

## How it Works

1. **Coordinate Compression:** We pair each element with its original index and sort these pairs by value. This allows the algorithm to work with any data type (integers, floats, or strings) and handles non-sequential numbers.

2. **Cycle Detection:** Any permutation can be decomposed into disjoint cycles.
    * If an element is already in its sorted position, it forms a cycle of length 1 (0 swaps).
    * For any other cycle of length $k$, the number of swaps needed to resolve it is $k - 1$.

3. **Efficiency:** By tracking `visited` elements, we ensure each element is processed exactly once.

## Algorithm Overview

* **Step 1:** Sort `enumerate(arr)` to determine the target positions.
* **Step 2:** Iterate through the array. If an element hasn't been visited, follow its "cycle" by jumping to the indices where each element belongs.
* **Step 3:** For every cycle found, increment the total swap count by `(cycle_size - 1)`.

## Complexity Analysis

| Complexity | Notation | Reason |
| :--- | :--- | :--- |
| **Time** | $O(n \log n)$ | Primary bottleneck is the initial sorting of the array. |
| **Space** | $O(n)$ | Requires extra space for the `visited` list and the sorted pairs. |

## Usage

```python
def minimum_swaps(arr):
    # Implementation logic
    ...

# Example with non-sequential integers
arr = [7, 1, 3, 2, 4, 5, 6]
result = minimum_swaps(arr)

print(f"Minimum swaps needed: {result}")
# Output: 5
