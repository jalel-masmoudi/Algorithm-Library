"""
Quick Sort Implementation
Time: O(n log n) average, O(n²) worst
Space: O(log n)
Stable: No
"""

def quick_sort(arr):
    """
    Sort array using quick sort algorithm
    
    Args:
        arr: List of comparable elements
    
    Returns:
        Sorted list
    
    Example:
        >>> quick_sort([3, 1, 4, 1, 5, 9])
        [1, 1, 3, 4, 5, 9]
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)


def quick_sort_inplace(arr, low=0, high=None):
    """In-place quick sort with better performance"""
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)
    
    return arr


def partition(arr, low, high):
    """Partition array around pivot"""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Test cases
if __name__ == "__main__":
    test_cases = [
        [3, 1, 4, 1, 5, 9, 2, 6],
        ,
        [],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5]
    ]
    
    for test in test_cases:
        result = quick_sort(test.copy())
        print(f"Input: {test}")
        print(f"Output: {result}")
        print(f"Correct: {result == sorted(test)}\n")

