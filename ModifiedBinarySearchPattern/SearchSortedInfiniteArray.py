#Given ana infinite sorted array(or array of unknown size), find if a given number "key" is present in the array.
#if present return index, else return -1
import math

class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index>=len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader, key):

    start = 0
    end = 1

    while reader.get(end)<key:
        newStart = start+1
        end+=(end-start+1)*2
        start = newStart

    return binary_search(reader, start, end, key)

def binary_search(reader, start, end, key):
    while start<=end:
        mid = start+(end-start)//2
        if reader.get(mid)==key:
            return mid
        elif reader.get(mid)>key:
            end=mid-1
        else:
            start=mid+1
    return -1


#Time Complexity: O(logN) + O(logN)
#Space Complexity: O(1)





def main():
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array(reader, 16))
    print(search_in_infinite_array(reader, 11))
    reader = ArrayReader([1, 3, 8, 10, 15])
    print(search_in_infinite_array(reader, 15))
    print(search_in_infinite_array(reader, 200))

main()