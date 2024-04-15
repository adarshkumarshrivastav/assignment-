# write a code that prompts the user to input two sets of characters.Then, print the union of these two sets.
def get_set_from_input():
    input_str = input("Enter characters separated by commas: ")
    return set(map(str.strip, input_str.split(',')))

def main():
    print("Enter the first set of characters:")
    set1 = get_set_from_input()

    print("Enter the second set of characters:")
    set2 = get_set_from_input()

    union_set = set1.union(set2)

    print("Union of the two sets:", union_set)

if __name__ == "__main__":
    main()
 