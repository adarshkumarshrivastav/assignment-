# write a code to check if a given string is a palindrome or not
string=input(("enter a letter:"))

if(string==string[::-1]):

      print("the letter is palindrome")
else:
      print("the letter is not palindrome")