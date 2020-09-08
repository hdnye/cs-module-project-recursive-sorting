# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    
    # Your code here


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # Check if only 1 element 
    if len(arr) <= 1:
        return arr
    
    # if arr > 1:
    if len(arr) > 1:
    # divide arr
        mid = len(arr) // 2
        # assign vars
        lhs=arr[:mid]
        rhs=arr[mid:]  
        # lhs & rhs iterators
        i = 0
        j = 0

        # new list iterator
        k = 0
        while i < len(lhs) and j < len(rhs):
            if lhs[i] < rhs[j]:
                arr[k] = lhs[i]
                i += 1
            else:
                arr[k] = rhs[j]
                j += 1

        # for remaining 
        while i < len(lhs):
            arr[k] = lhs[i]
            i += 1
            k += 1
        while j < len(rhs):
            arr[k] = rhs[j]
            j += 1
            k += 1

     # merge sorted halves
    merge_sort(arr)      
    return arr   

    

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass


# Quick sort
nums = [29, 84, 35, 22, 64, 97, 8, 83, 46, 58]

def quicksort(arr):
     # stop when there's only 1 element left in the arr
    if len(arr) <= 1:
         return arr

    left, pivot, right = partition(arr) 

    sorted_left = quicksort(left)
    sorted_right = quicksort(right)

    sorted = sorted_left + [pivot] + sorted_right
    return sorted


def partition(arr):
    # choose pivot
    pivot = arr[0]

    # divide array into chunks
    left = []
    right = []
    
    # < on LHS, > on RHS
    for el in arr[1:]:
        if el < pivot:
            left.append(el)
        if el >= pivot:
            right.append(el)
    return left, pivot, right
    
print(quicksort(nums))
