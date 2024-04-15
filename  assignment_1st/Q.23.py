#  write a code to concatenate two tuples. The function should take two tuples as inputs and return a new tuple containing elements from both inputs tuples

def concatenate_tuples(tuple1, tuple2):

    concatenated_tuple = tuple1 + tuple2
    return concatenated_tuple
    
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

concatenated_result = concatenate_tuples(tuple1, tuple2)
print("Concatenated tuple:", concatenated_result)
