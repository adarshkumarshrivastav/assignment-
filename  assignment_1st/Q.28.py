# create a code that defines two sets of integers.Then,print the union,intersection,and differences of these two sets.
def main():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    union_set = set1.union(set2)
    print("Union of the two sets:", union_set)

    intersection_set = set1.intersection(set2)
    print("Intersection of the two sets:", intersection_set)

    difference_set1 = set1.difference(set2)
    print("Difference between set1 and set2:", difference_set1)

    difference_set2 = set2.difference(set1)
    print("Difference between set2 and set1:", difference_set2)

if __name__ == "__main__":
    main()
