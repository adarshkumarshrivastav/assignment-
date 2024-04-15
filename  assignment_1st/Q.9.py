# write a code to count the number of words in a string 
def count_words(s):
     words = s.strip().split()
     return len(words)

input_string = "This is a sample sentence to count words"
word_count = count_words(input_string)
print("Number of words in the string:", word_count)
