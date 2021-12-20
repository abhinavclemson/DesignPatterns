
#Given a Bitonic array, find if a given "key" is present in it.
#An aray is considered bitonic if it is monotonically increasing and then monotonically
#decreasing.


#Monotonically increasing or decreasing means that for any index i in the array
#arr[i]!=arr[i+1]

def search_bitonic_array(arr, key):

      start = 0
      end = len(arr)-1
      #STEP1: Using bitonic array method to find the max element index
      maxElementIndex = find_max_element(arr)

      #STEP_2: use traditional binary search method.
      #NOTE: Always send start_index and end_index in that method,
      # otherwise the returned index would be incorrect.
      lowerHalf = binary_search(arr, 0, maxElementIndex, key)
      upperHalf = binary_search(arr, maxElementIndex+1, len(arr)-1, key, isAscending = False)
      index = max(lowerHalf, upperHalf)

      #Step_3: Incase both the returned results are -1, that means the key was not found.
      #and value cannot be lower than -1, so we can use max(lowerHalf, UpperHalf) and if we get -1
      #that means both halves returned -1 and the key doesn't exist.
      return index if index!=-1 else -1





#Order-agnostic Binary search
def binary_search(arr, start, end, key, isAscending=True):

    while start<=end:
        mid = start+(end-start)//2
        if arr[mid]==key:
            return mid

        if isAscending:
            if arr[mid]>key:
                end = mid-1
            else:
                start = mid+1
        else:
            if arr[mid]>key:
                start = mid+1
            else:
                end = mid-1


    return -1


def find_max_element(arr):
    start = 0
    end = len(arr)-1

    #We are using bitonic array max element method here,
    #and we are using start<end, instead of traditional start<=end,
    #because we want the exact index of the peak of the array,
    #and when start==end the loop would break and return the max element in the array.
    while start<end:
        mid = start+(end-start)//2

        #if the next element of the value at mid is less than the value at mid.
        #It means that we are in the upperHalf descending array
        #and it is quite possible that value at mid is the peak in this array.
        #So we cannot omit it, like traditional binary search.
        #Therefore we set the end to mid here.
        if arr[mid]>arr[mid+1]:
            end = mid

        #and if the value at mid is less than the next element, that means we are in the
        #lowerHalf ascending array, and we cannot omit the possibility that value at mid+1
        #is the peak. So we set the start value to mid+1
        else:
            start = mid+1

    #When start==end condition is met, then the loop would break, peak value is returned.
    return start






def main():
  print(search_bitonic_array([1, 3, 8, 4, 3], 4))
  print(search_bitonic_array([3, 8, 3, 1], 8))
  print(search_bitonic_array([1, 3, 8, 12], 12))
  print(search_bitonic_array([10, 9, 8], 10))


main()

#Time Complexity: O(logN)
#Space Complexity: O(1)