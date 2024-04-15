# write a code that takes a list of words as inputs and returns a dictionary where the keys are unique words and the values are the frequencies of those words in the inputs list
def word_frequency(words):
    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
    return frequency_dict

def main():
    input_words = input("Enter words separated by spaces: ").split()
    frequencies = word_frequency(input_words)
    print("Word frequencies:")
    for word, frequency in frequencies.items():
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()
