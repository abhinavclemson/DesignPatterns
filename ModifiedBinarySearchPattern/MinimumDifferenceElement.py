
def search_min_diff_element(arr, key):

    start = 0
    end = len(arr)-1

    while start<=end:
        mid = start + (end-start)//2
        if key==arr[mid]:
            return key
        elif key<arr[mid]:
            end = mid-1
        else:
            start = mid+1

    lowerVal = arr[end] if 0<=end<len(arr) else float(-'inf')
    upperVal = arr[start] if 0<=start<len(arr) else float('inf')

    if (key-lowerVal)>(upperVal-key):
        return upperVal

    return lowerVal

# Time complexity: O(logN)
# Space complexity: O(1)


def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))

main()