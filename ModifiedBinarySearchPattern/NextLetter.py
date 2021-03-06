# Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array
#greater than a given "key".
#assume the given array is a circular list


def search_next_letter(letters, key):

    start = 0
    end = len(letters)-1

    while start<=end:
        mid = start+ (end-start)//2
        if letters[mid]<=key:
            start = mid+1
        else:
            end = mid-1

    return letters[start%len(letters)]

def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))

main()


#Time Complexity: O(logN)
#Space Complexity: O(1)
