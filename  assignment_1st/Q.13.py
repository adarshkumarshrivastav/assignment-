# create a code to count the occurrences of each element in a list and return a dictionary with elememt keys and their counts as values.
def count_occurrences(lst):
    occurrences = {}
    for item in lst:
        occurrences[item] = occurrences.get(item, 0) + 1
    return occurrences

numbers = [1, 2, 3, 4, 2, 1, 3, 2, 4, 5, 2]
occurrences_dict = count_occurrences(numbers)
print("Occurrences:", occurrences_dict)
