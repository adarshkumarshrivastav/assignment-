# develop a code  that prompts the use to inputs two sets of strings.Then,prints the symmetric difference of these two sets.
def get_set_from_input():
    input_str = input("Enter strings separated by commas: ")
    # Split the input string by commas and strip any leading/trailing whitespace
    return set(map(str.strip, input_str.split(',')))

def main():
    print("Enter the first set of strings:")
    set1 = get_set_from_input()

    print("Enter the second set of strings:")
    set2 = get_set_from_input()

    symmetric_difference_set = set1.symmetric_difference(set2)

    print("Symmetric difference of the two sets:", symmetric_difference_set)

if __name__ == "__main__":
    main()
