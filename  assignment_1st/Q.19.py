#  create a code to find the union of two lists without duplicates
def union(list1, list2):
    union_set = set(list1 + list2)

    union_list = list(union_set)

    return union_list

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

union_result = union(list1, list2)
print("Union:", union_result)
