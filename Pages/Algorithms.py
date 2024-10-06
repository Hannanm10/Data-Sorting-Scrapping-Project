##MergeSort
def merge_sort(data, column_index):
    """Sorts a 2D list based on the specified column index using the merge sort algorithm."""
    if len(data) > 1:
        mid = len(data) // 2  # Finding the mid of the array
        left_half = data[:mid]  # Dividing the elements into 2 halves
        right_half = data[mid:]

        merge_sort(left_half, column_index)  # Sorting the first half
        merge_sort(right_half, column_index)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i][column_index] < right_half[j][column_index]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

    return data

def quick_sort(arr, column):
    """Quick Sort algorithm."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][column]  # Choose the middle element as the pivot
    left = [x for x in arr if x[column] < pivot]
    middle = [x for x in arr if x[column] == pivot]
    right = [x for x in arr if x[column] > pivot]
    return quick_sort(left, column) + middle + quick_sort(right, column)

def counting_sort_strings(arr, position):
    max_length = max(len(s) for s in arr)  # Find the maximum string length
    count = [0] * 256  # Adjust size based on expected character range (ASCII)
    output = [''] * len(arr)

    for string in arr:
        char_index = ord(string[position]) if position < len(string) else 0  # Handle shorter strings
        if char_index >= len(count):  # Check if the char_index exceeds the count array size
            # Expand count array if needed
            count.extend([0] * (char_index - len(count) + 1))  # Ensure count can handle this char_index
        count[char_index] += 1

    # Update count array to hold actual positions
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(len(arr) - 1, -1, -1):
        char_index = ord(arr[i][position]) if position < len(arr[i]) else 0
        output[count[char_index] - 1] = arr[i]
        count[char_index] -= 1

    return output  # Return the sorted array


def radix_sort_strings(arr):
    max_length = max(len(s) for s in arr)  # Find the maximum length of the strings

    for position in range(max_length - 1, -1, -1):  # Sort by each character position
        arr = counting_sort_strings(arr, position)  # Sort based on the current character position

    return arr  # Return the sorted array

def bucket_sort(arr):
    if not arr:
        return arr

    # Determine if the data is numeric or string
    is_numeric = all(isinstance(x, (int, float)) for x in arr)

    # Create buckets based on the type of data
    if is_numeric:
        max_value = max(arr)
        bucket_count = len(arr) // 5  # You can adjust the bucket count as needed
        buckets = [[] for _ in range(bucket_count)]

        # Distribute the elements into buckets
        for num in arr:
            index = num * bucket_count // (max_value + 1)  # Determine the bucket index
            buckets[index].append(num)

        # Sort each bucket and concatenate
        sorted_array = []
        for bucket in buckets:
            sorted_array.extend(sorted(bucket))  # Sort the bucket and add it to the result

    else:
        # For strings, determine the maximum length for the buckets
        max_length = max(len(s) for s in arr)
        buckets = [[] for _ in range(max_length + 1)]  # Create a bucket for each string length

        # Distribute strings into buckets based on their length
        for s in arr:
            buckets[len(s)].append(s)

        # Sort each bucket and concatenate
        sorted_array = []
        for bucket in buckets:
            sorted_array.extend(sorted(bucket))  # Sort the bucket and add it to the result

    return sorted_array

def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Compare and swap if the element found is greater than the next element
            if str(arr[j]) > str(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            # Use natural comparison for digits and string comparison for strings
            if (isinstance(arr[j], str) and isinstance(arr[min_index], str) and arr[j] < arr[min_index]) or \
               (isinstance(arr[j], (int, float)) and isinstance(arr[min_index], (int, float)) and arr[j] < arr[min_index]) or \
               (isinstance(arr[j], (int, float)) and isinstance(arr[min_index], str)):
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and (str(arr[j]) > str(key)):
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr

def insertion_sort_tim(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key

def merge_tim(arr, left, mid, right):
    # Create temporary arrays
    left_half = arr[left:mid + 1]
    right_half = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    # Merge the temporary arrays back into arr[left:right + 1]
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Copy any remaining elements of left_half, if there are any
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Copy any remaining elements of right_half, if there are any
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

def tim_sort(arr):
    min_run = 32  # Define a minimum run size

    # Sort individual subarrays of size RUN
    for start in range(0, len(arr), min_run):
        end = min(start + min_run - 1, len(arr) - 1)
        insertion_sort_tim(arr, start, end)

    size = min_run
    # Merge the sorted subarrays
    while size < len(arr):
        for left in range(0, len(arr), size * 2):
            mid = min(len(arr) - 1, left + size - 1)
            right = min((left + 2 * size - 1), (len(arr) - 1))

            if mid < right:  # If there are elements to merge
                merge_tim(arr, left, mid, right)
        
        size *= 2

    return arr  # return the sorted array

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)  # Heapify the root element

    return arr  # return the sorted array


