def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration
   
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
   
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    mid = int(len(array)/2)
    left = array[mid-1]
    right = array[mid + 1]
    if array[mid] == target:
        return mid
    else:
        if target >left:
            return mid+binary_search(array[mid:len(array)],target)
        else:
            return binary_search(array[0:mid],target)
    pass

def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)