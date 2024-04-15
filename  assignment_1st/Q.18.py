# implement a code to find the intersection of two given lists.
def intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    intersection_set = set1.intersection(set2)

    intersection_list = list(intersection_set)

    return intersection_list

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

intersection_result = intersection(list1, list2)
print("Intersection:", intersection_result)
