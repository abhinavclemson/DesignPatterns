# Find the maximum value in a given Bitonic array.
# An array is considered bitonic if it is monotonically increasing and then monotonically decreasing.
# Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

def find_max_in_bitonic_array(arr):
    start=0
    end = len(arr)-1

    while start<end: #observe here that, it breaks when start=end
        mid = start + (end-start)//2
        if arr[mid]>arr[mid+1]:
            #if value at mid is greater than mid+1, that means we are in the upper half of array which is descending.
            end = mid
        else:
            #if value at id is lower than mid+1, that means we are in the lower half of array which is ascending.
            start = mid+1

    #at last returning the array[start] because it is the required number
    #as start=end, and arr[start] is the greatest number of all the element
    return arr[start]



def main():
  print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
  print(find_max_in_bitonic_array([3, 8, 3, 1]))
  print(find_max_in_bitonic_array([1, 3, 8, 12]))
  print(find_max_in_bitonic_array([10, 9, 8]))


main()

#Time Complexity: O(logN)
#Space Complexity: 0(1)
