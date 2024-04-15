# write a code that takes a dictionary as input and returns a sorted version of it based on the values. you can choose whether to sort in ascending or descending order.
def sort_dict_by_values(input_dict, reverse=False):

    sorted_items = sorted(input_dict.items(), key=lambda x: x[1], reverse=reverse)
    
    sorted_dict = dict(sorted_items)
    
    return sorted_dict

input_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}

sorted_dict_asc = sort_dict_by_values(input_dict)
print("Sorted dictionary (ascending order):", sorted_dict_asc)

sorted_dict_desc = sort_dict_by_values(input_dict, reverse=True)
print("Sorted dictionary (descending order):", sorted_dict_desc)
