
# given an arr and num - search if that num exits in arr or not? if exists return index else -1


# liner method
def search(arr, num):
    index = 0
    for i in arr:
        if i == num:
            return index
        index += 1
    return -1


# binary search
def binarySearch(arr, num):
    start = 0
    end = len(arr)-1
    mid = (start+end)/2
    while start <= end:
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            end = mid-1
        else:
            start = mid+1

        mid = (start + end) / 2
    return -1


number = 10
array = [1, 2, 5, 6, 7, 8]
# call the method
print search(array,number)
print binarySearch(array,number)