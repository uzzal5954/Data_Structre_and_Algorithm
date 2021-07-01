# binary search implimention by recursive
def binary_search(array, x, low, high):
    # low = 0
    # high = len(array) - 1

    if high >= low:
        mid = (low + high)//2
    
        if (x == array[mid]):
            print("value is found in index ", mid)
            return
        
        elif (x > array[mid]):
            # low = mid + 1
            return binary_search(array, x, mid + 1, high)
        
        elif(x < array[mid]):
            # high = mid - 1
            return binary_search(array, x, low, mid - 1)

    print("value is not found")


array = [10, 11, 13, 15, 20, 25, 30, 52]
x = 52
binary_search(array, x, 0, len(array)-1)   
