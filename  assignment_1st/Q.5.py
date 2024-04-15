# # write a code to find all the  occurrences of a given substring within another string
def find_all_occurrences(main_string, substring):
    occurrences = []
    start = 0
    while True:
        start = main_string.find(substring, start)
        if start == -1:
            break
        occurrences.append(start)
        start += 1
    return occurrences

main_string = "abracadabra"
substring = "abra"
print("Occurrences of '{}' in '{}':".format(substring, main_string))
print(find_all_occurrences(main_string, substring))
