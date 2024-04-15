# write a code to reverse a list in- place without using  any built-in reverse functions
def reverse_list_in_place(lst):
    start_index = 0
    end_index = len(lst) - 1

    while start_index < end_index:
        
        lst[start_index], lst[end_index] = lst[end_index], lst[start_index]
        
        start_index += 1
        end_index -= 1
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
reverse_list_in_place(my_list)
print("Reversed list:", my_list)
