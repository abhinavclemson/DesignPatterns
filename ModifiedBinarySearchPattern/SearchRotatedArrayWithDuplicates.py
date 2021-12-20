def search_rotated_with_duplicates(arr, key):

    start = 0
    end = len(arr)-1

    while start<=end:
        mid = start+(end-start)//2

        if arr[mid]==key:
            return mid

        #if all values at start, mid and end are same:
        if arr[start]==arr[mid] and arr[mid]==arr[end]:
            start+=1
            end-=1

        elif arr[start]<=arr[mid]: #It is means that the left side is ascending

            if arr[start]<=key and key<arr[mid]:
                end = mid-1
            else:
                start = mid+1

        else:

            if arr[mid]<key and key<=arr[end]: #if key exists, it would be on this side
                start = mid+1
            else:
                end = mid-1

    return -1








def main():
    print(search_rotated_with_duplicates([3, 7, 3, 3, 3], 7))

main()

#Time Complexity: O(logN)
#Space Complexity: O(1) as we are using iterative approach, not recursive.

