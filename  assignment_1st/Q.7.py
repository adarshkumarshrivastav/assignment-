# write a code to determine if a string has all unique characters.
def has_unique_characters(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

test_string1 = "abcdefg"
test_string2 = "hello"
print("Does '{}' have all unique characters?".format(test_string1), has_unique_characters(test_string1))
print("Does '{}' have all unique characters?".format(test_string2), has_unique_characters(test_string2))
