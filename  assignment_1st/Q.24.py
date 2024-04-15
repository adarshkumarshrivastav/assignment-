# develop a code that prompts the user to input two sets of strings.Then,print the elements that are present in the first set but not in the second set
def get_set_from_input():
    input_str = input("Enter strings separated by commas: ") 
    return set(map(str.strip, input_str.split(',')))

def main():

    print("Enter the first set of strings:")
    set1 = get_set_from_input()

    print("Enter the second set of strings:")
    set2 = get_set_from_input()

    difference_set = set1 - set2

    print("Elements present in the first set but not in the second set:", difference_set)

if __name__ == "__main__":
    main()
