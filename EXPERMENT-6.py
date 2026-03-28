def binary_search(arr, key, low, high):
    # If the range becomes invalid, the element is not present
    if low > high:
        return -1

    # Find the middle index
    mid = (low + high) // 2

    # Check if the middle element is the key
    if arr[mid] == key:
        return mid

    # If key is smaller, search in the left half
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)

    # Otherwise, search in the right half
    else:
        return binary_search(arr, key, mid + 1, high)


# Example
arr = [2, 3, 4, 10, 40]
key = 10

index = binary_search(arr, key, 0, len(arr) - 1)

if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found")