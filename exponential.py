def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    bound = 1
    while bound < n and arr[bound] < target:
        bound *= 2
    return binary_search(arr[:min(bound, n)], target)
