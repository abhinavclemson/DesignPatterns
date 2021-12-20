# Given an array of number sorted in an ascending order, find the ceiling of a given number "key".
# The ceiling of the "key" wil be the smallest element in the given array greater than or equal to the "key".


def search_ceiling_of_a_number(arr, key):
    #Here we will use binary search
    start = 0
    end = len(arr)-1
    #if there is no value in the array which is greater than the key
    if key>arr[end]:
        return -1
    while start<=end:
        mid = start + (end-start)//2 #so the adding of two numbers doesn't exceed the max integer value
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            end = mid-1
        else:
            start = mid+1

    return start







def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))

main()
