def minimum_swaps(arr):
    n = len(arr)
    sorted_arr = sorted(arr)
    index_map = {value: idx for idx, value in enumerate(sorted_arr)}
    visited = [False] * n
    swaps = 0

    for i in range(n):
        if visited[i] or index_map[arr[i]] == i:
            # Already in correct position or visited
            continue

        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = index_map[arr[j]]  # move to index where arr[j] should go
            cycle_size += 1

        if cycle_size > 0:
            swaps += (cycle_size - 1)

    return swaps
