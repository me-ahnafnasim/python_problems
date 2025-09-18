"""def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        # Store the current element
        key = arr[i]
        #print("element", key)
        # Initialize the index for the sorted portion
        j = i - 1
        #print("j",j)
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key in its correct position
        arr[j + 1] = key

# Example usage
if __name__ == "__main__":
    data = [12, 11, 13, 5, 6]
    print("Original array:", data)
    insertion_sort(data)
    print("Sorted array:", data)"""

       

def InsertionSort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j
        while i > 0 and a[i-1] > key:
              a[i] = a[i-1]
              i = i - 1
              a[i] = key
              
    return a


if __name__ == "__main__":
     a=[4,1,78,93]
     print("orginal arrar data",a)
     InsertionSort(a)
     print("array after modify", a)
