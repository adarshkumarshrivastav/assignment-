# create a code that takes a tuple and two integers as input.The function should return a new tuple containing elements from the original tuple within the specified range of indicies.
def slice_tuple(input_tuple, start_index, end_index):

    start_index = max(0, min(start_index, len(input_tuple)))
    end_index = max(0, min(end_index, len(input_tuple)))
    
    sliced_tuple = input_tuple[start_index:end_index]

    return sliced_tuple

original_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
start_index = 2
end_index = 6

sliced_result = slice_tuple(original_tuple, start_index, end_index)
print("Sliced tuple:", sliced_result)
