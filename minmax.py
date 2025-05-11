def minmax(arr, low, high):
    if low == high:
        return arr[low], arr[low]
        
    if high == low + 1:
        if arr[low] > arr[high]:
            return arr[high], arr[low]
        else:
            return arr[low], arr[high]
    
    
    mid = (low + high) // 2
    
    left_min, left_max = minmax(arr, low, mid)
    right_min, right_max = minmax(arr, mid + 1, high)
    
    return min(left_min, right_min), max(left_max, right_max)
    

n = int(input("Enter N: "))

arr = list(map(int, input("Enter elements: ").split()))

minimum, maximum = minmax(arr, 0, n -1)

print("Maximum element:", maximum)
print("Minimum element:", minimum)