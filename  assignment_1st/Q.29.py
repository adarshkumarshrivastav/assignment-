# write a code that takes a tuple and an element as input. The function should return the count of occurrences of the given in the tuple.
def count_occurrences(input_tuple, element):
    
    occurrences = input_tuple.count(element)
    return occurrences
input_tuple = (1, 2, 3, 4, 2, 2, 5)
element = 2
occurrences = count_occurrences(input_tuple, element)
print("Number of occurrences of", element, "in the tuple:", occurrences)
