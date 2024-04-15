# write a code to remove all occurrences of a specific element  from a list 
def remove_element(lst, element):
    return [x for x in lst if x != element] 
    
original_list = [1, 2, 3, 4, 2, 5, 6, 2]
element_to_remove = 2
new_list = remove_element(original_list, element_to_remove)
print("Original list:", original_list)
print("List after removing {}:".format(element_to_remove), new_list)
