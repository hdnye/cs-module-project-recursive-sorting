import sys

sys.setrecursionlimit(10**6)

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    
    # Your code here
    # set iterators 
    i = 0
    j = 0    
    # set vars for len(arr[x])    
    arr1 = len(arrA)
    arr2 = len(arrB)    
    arr = []

    # while loop to iterate all el's
    # compare el's & append to merged list
    while (i < arr1) and (j < arr2):
        if(arrA[i]) < (arrB[j]):
            arr.append(arrA[i])
    # increment from list    
            i += 1  
    # else stmt to append 2nd list          
        else: 
            arr.append(arrB[j])
            j += 1
    # if stmt to append list if any el's remain
    if i == arr1:
        arr.extend(arrB[j:])
    else: 
        arr.extend(arrA[i:])
 
    return arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # Check if only 1 element 
    if len(arr) <= 1:
        return arr
    
    if len(arr) > 1:
    # divide arr
        mid = len(arr) // 2

    return merge(merge_sort(arr[mid:]), merge_sort(arr[:mid]))        
                      
     
       

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
