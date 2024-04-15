# write a code that takes two dictionaries as inputs and merges them into a single dictinary. if there are common keys,the values  should be added together.
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()

    for key, value in dict2.items():
        if key in merged_dict:

            merged_dict[key] += value
        else:
            merged_dict[key] = value
    
    return merged_dict

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}

merged_result = merge_dictionaries(dict1, dict2)
print("Merged dictionary:", merged_result)
