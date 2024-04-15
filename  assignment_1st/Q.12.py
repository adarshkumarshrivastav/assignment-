# implement a code to find the second largest number in a given list of integers 
def second_largest_number(lst):
    if len(lst) < 2:
        return "List must contain at least two elements"
    sorted_list = sorted(lst)
    return sorted_list[-2]

numbers = [10, 5, 20, 15, 30]
second_largest = second_largest_number(numbers)
print("Second largest number:", second_largest)
