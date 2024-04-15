# write a code to check if two given strings are anagrams of each other

str1 = "race"
str2= "care"

str1 = str1.lower()
str2 = str2.lower()

if len(str1) == len(str2):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    if sorted_str1 == sorted_str2:
     print(f"{str1} and {str2} are anagrams of each other")
else:
    print(f"{str1} and {str2} are not anagrams of each other")