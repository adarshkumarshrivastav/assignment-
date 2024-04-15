# implement a code to find and remove duplicates from a list while preserving the original order of elements

def remove_duplicates_preserve_order(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

original_list = [1, 2, 3, 2, 4, 5, 1, 6, 7, 7, 8]
unique_elements = remove_duplicates_preserve_order(original_list)
print("Original list:", original_list)
print("List with duplicates removed while preserving order:", unique_elements)
