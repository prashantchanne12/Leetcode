def sqauredSortedArrays(arr):
    n = len(arr)
    left = 0
    right = n-1
    highestIndex = right
    newArr = [0 for i in range(n)]

    while left <= right:
        lefSquare = arr[left]*arr[left]
        rightSquare = arr[right]*arr[right]

        if lefSquare > rightSquare:
            newArr[highestIndex] = lefSquare
            left += 1
        else:
            newArr[highestIndex] = rightSquare
            right -= 1

        highestIndex -= 1

    return newArr


arr = [-2, -1, 0, 2, 3]
print(sqauredSortedArrays(arr))
