# reverse a array using recursion
arr = [1,2,3,4,5,6,7,8,9]

def reverse(arr, left, right):
    if left >= right:
        return

    arr[left], arr[right] = arr[right], arr[left]
    reverse(arr, left + 1, right - 1)

reverse(arr, 0, len(arr) - 1)
print(arr)