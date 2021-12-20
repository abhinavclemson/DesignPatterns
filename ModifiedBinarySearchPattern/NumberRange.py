#Given an array of number sorted in ascending order, find the range of a given number "key".
#The range of the 'key' will be the first and the last position of the 'key' in the array.

def find_range(arr, key):


    upperIndex = findMaxIndex(arr, key)
    lowerIndex = findMaxIndex(arr, key, upperLimit=False)

    return [lowerIndex, upperIndex]


def findMaxIndex(arr, key, upperLimit=True):

    start = 0
    end = len(arr)-1
    keyIndex = -1
    while start<=end:
        mid = start+(end-start)//2
        if arr[mid]<key:
            start = mid+1
        elif arr[mid]>key:
            end = mid-1
        else:
            #core concept, understand this one.
            keyIndex = mid
            if upperLimit:
                start = mid+1
            else:
                end = mid-1

    return keyIndex


def main():
  print(find_range([4, 6, 6, 6, 9], 6))
  print(find_range([1, 3, 8, 10, 15], 10))
  print(find_range([1, 3, 8, 10, 15], 12))


main()


#Time Complexity: O(logN)
#Space Complexity: O(1)