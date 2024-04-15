# write a code to shuffle a given list randomly without using any built_in shuffle functions 
import random

def shuffle_list(input_list):
    shuffled_list = input_list[:] 
    for i in range(len(shuffled_list) - 1, 0, -1):

        j = random.randint(0, i)
        
        shuffled_list[i], shuffled_list[j] = shuffled_list[j], shuffled_list[i]

    return shuffled_list

original_list = [1, 2, 3, 4, 5]
shuffled_result = shuffle_list(original_list)
print("Original List:", original_list)
print("Shuffled List:", shuffled_result)
