                                           ##bubble sort
     
def BubbleSort(array, start, end):
    for i in range(start, end):
        for j in range(start, end - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                
                
                
                                          ##Selection sort

def SelectionSort(array, start, end):
    for i in range(start, end - 1):
        min_index = i
        for j in range(i + 1, end):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        
        
        
                                           ##insertion sort

def InsertionSort(array, start, end):
    for i in range(start + 1, end):
        key = array[i]
        j = i - 1
        while j >= start and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        
        
        
                                             ##Merge sort

def MergeSort(array, start, end):
    if start < end:
        middle = (start + end) // 2
        MergeSort(array, start, middle)
        MergeSort(array, middle + 1, end)
        Merge(array, start, middle, end)
        
def Merge(array, p, q, r):
    left_half_array = array[p:q + 1]  
    right_half_array = array[q + 1:r + 1]  
    
    i = j = 0  
    k = p      

    while i < len(left_half_array) and j < len(right_half_array):
        if left_half_array[i] <= right_half_array[j]:
            array[k] = left_half_array[i]
            i += 1
        else:
            array[k] = right_half_array[j]
            j += 1
        k += 1
    while i < len(left_half_array):
        array[k] = left_half_array[i]
        i += 1
        k += 1
    while j < len(right_half_array):
        array[k] = right_half_array[j]
        j += 1
        k += 1
        

                                       ##quick sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) - 1]
        less_than_pivot = [x for x in arr[:-1] if x <= pivot]
        greater_than_pivot = [x for x in arr[:-1] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
    
    
    

                                        ##Count Sort

def counting_sort(arr):

    max_val = max(arr)
    count_arr = [0] * (max_val + 1)
    for num in arr:
        count_arr[num] += 1

    sorted_index = 0
    for i in range(len(count_arr)):
        while count_arr[i] > 0:
            arr[sorted_index] = i
            sorted_index += 1
            count_arr[i] -= 1
    
    return arr


                                        ##Radix Sort
                                        

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)

    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


                                      ##Bucket sort
                                  
def bucket_sort(arr):
    
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]
    for num in arr:
        index = int(num_buckets * num)
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array


                                  ##Shell sort
                                  
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]

            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                
            arr[j] = temp
        gap //= 2

      
                                  ##Comb Sort
                                  
def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3  
    sorted = False

    while not sorted:
        gap = int(gap // shrink)
        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:

                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False 
            i += 1
            
