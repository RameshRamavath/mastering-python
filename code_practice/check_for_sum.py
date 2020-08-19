# given an array and sum, check if adding any two elements in Array gives that sum
# example:: Array(1,3,6,2,8,5), sum = 11 --> Answer: boolean Yes


def checkForSum(arr, req_sum):

    # Set to store visited elements
    lookup_set = set()
    # check the diff and lookup in collection if we already seen that diff
    for element in arr:
        delta = req_sum - element
        if lookup_set.__contains__(delta):
            return True
        else:
            lookup_set.add(element)

    return False


if __name__ == '__main__':
    arr = [1,3,6,2,8,5]
    # call our method
    print(checkForSum(arr, 11))  # True
    print(checkForSum(arr, 20))  # False
