# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here 
    
    # check for empty list
    if arr is None:
        return False

    # base case
    if end >= start:       
        mid = (start + end) // 2

        # compare to target
        if target == arr[mid]:        
            return mid
        # else move left       
        elif target < arr[mid]:
            return binary_search(arr, target, start, mid -1)
        # else move right
        else:
            return binary_search(arr, target, mid + 1, end)  
    else: 
        return - 1         

   

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here

