#Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number,
# find if a given ‘key’ is present in it.


def search_rotated_array(arr,key):

    start =0
    end = len(arr)-1
    while start<=end:
        mid = start+(end-start)//1
        if arr[mid]==key:
            return mid

        #STEP-1: Try to check which side is in ascending order
        if arr[start]>=arr[mid]: #that means right side is in ascending order

            #STEP-2: Try to check if the key falls into which side

            #Note: we don't need to check for key>=arr[mid]
            #Why? because if arr[mid] was equal to key, then that value would have been returned.
            if key>arr[mid] and key<=arr[end]:
                start = mid+1
            else:
                end = mid-1

        else: #that means left side is in ascending order

            if key>=arr[start] and key<arr[mid]:
                end = mid-1
            else:
                start = mid+1

    return -1




def main():
  print(search_rotated_array([10, 15, 1, 3, 8], 15))
  print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))

main()

