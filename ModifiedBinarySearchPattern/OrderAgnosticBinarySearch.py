

def binary_search(arr, key):
    left = 0
    right = len(arr)-1
    isAscending = True if arr[left]<arr[right] else False

    while left<=right:
        # mid = (left+right)
        mid = (left + (right-left)//2) #why? if the left+right value is bigger than integer.MAX_VALUE,the above equation can show an error
        if arr[mid]==key:
            return mid
        if isAscending:
            if arr[mid]<key:
                left = mid+1
            else:
                right = mid-1
        else:
            if arr[mid]>key:
                left = mid+1
            else:
                right = mid-1

    return -1

def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))


main()

#Time complexity: O(logn) and space complexity: 0(1)
