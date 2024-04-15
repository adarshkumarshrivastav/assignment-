#  create code to check if a given is sorted (either in ascending or descending order) or not.
def is_sorted(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        return "Ascending"
    if all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)):
        return "Descending"

    return "Not sorted"

arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 4, 3, 2, 1]
arr3 = [1, 3, 2, 5, 4]

print("Array 1 is", is_sorted(arr1))
print("Array 2 is", is_sorted(arr2))
print("Array 3 is", is_sorted(arr3))
