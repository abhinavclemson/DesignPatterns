
def search_floor_of_a_number(arr, key):

    start=0
    end = len(arr)-1

    if arr[start]>key:
        return -1

    while start<=end:
        mid = start + (end-start)//2 #so that mid value doesn't exceed the maximum integer value allowed

        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            end = mid-1
        else:
            start = start+1

    return end










def main():
  print(search_floor_of_a_number([4, 6, 10], 6))
  print(search_floor_of_a_number([1, 3, 8, 10, 15], 12))
  print(search_floor_of_a_number([4, 6, 10], 17))
  print(search_floor_of_a_number([4, 6, 10], -1))

main()


