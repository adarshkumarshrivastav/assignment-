 # write a code that takes two tuples as input and returns a new tuple containing elements that are common to both input tuples.
def common_elements(tuple1, tuple2):
    set1 = set(tuple1)
    set2 = set(tuple2)

    
    common_set = set1.intersection(set2)

    common_tuple = tuple(common_set)

    return common_tuple

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

common_result = common_elements(tuple1, tuple2)
print("Common elements:", common_result)
