# write a code to concatenate two strings without using the + operator 
def concatenate_strings(str1, str2):
    return "{}{}".format(str1, str2)
string1 = "Hello"
string2 = "World"
concatenated_string = concatenate_strings(string1, string2)
print("Concatenated string:", concatenated_string)
