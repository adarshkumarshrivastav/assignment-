# write a code to access a value in a nested dictinary. the functin should take the dictinary and a list of keys as input,and return the corresponding value. if any of the keys do not exist in the dictionary,the function should return none.
def get_value_nested_dict(nested_dict, keys):
    current_dict = nested_dict
    
    for key in keys:
        if key in current_dict:
            current_dict = current_dict[key]
        else:
        
            return None
    
    return current_dict
nested_dict = {
    'a': {
        'b': {
            'c': 10,
            'd': 20
        }
    },
    'x': {
        'y': 30,
        'z': 40
    }
}

keys = ['a', 'b', 'c']
value = get_value_nested_dict(nested_dict, keys)
print("Value corresponding to keys {}: {}".format(keys, value))

keys_not_present = ['a', 'b', 'x']  
value_not_present = get_value_nested_dict(nested_dict, keys_not_present)
print("Value corresponding to keys {}: {}".format(keys_not_present, value_not_present))
