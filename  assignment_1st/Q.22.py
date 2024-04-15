#   create a code that prompts the user to enter two sets of intergers separated by commas.Then,print the intersection of these two sets

def get_set_from_input():
    input_str = input("Enter integers separated by commas: ")
    return set(map(int, input_str.split(',')))

def main():
    print("Enter the first set:")
    set1 = get_set_from_input()

    print("Enter the second set:")
    set2 = get_set_from_input()

    
    intersection_set = set1.intersection(set2)


    print("Intersection of the two sets:", intersection_set)

if __name__ == "__main__":
    main()
