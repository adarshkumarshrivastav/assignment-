 # write a code to convert a given string to uppercase or lowercase
def convert_to_uppercase(s):
    return s.upper()

def convert_to_lowercase(s):
    return s.lower()
    
input_string = "Hello World"
uppercase_string = convert_to_uppercase(input_string)
lowercase_string = convert_to_lowercase(input_string)

print("Original string:", input_string)
print("Uppercase string:", uppercase_string)
print("Lowercase string:", lowercase_string)
