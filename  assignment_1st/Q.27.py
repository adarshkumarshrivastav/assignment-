# develop a code that takes a tuple of integers as inputs. The function should return the maximum and minimum values from the tuple using unpacking. 
def find_max_min(input_tuple):

    max_value = max(input_tuple)
    min_value = min(input_tuple)
    
    return max_value, min_value

input_tuple = (10, 5, 7, 2, 15, 3)
max_value, min_value = find_max_min(input_tuple)
print("Maximum value:", max_value)
print("Minimum value:", min_value)
