# write a code to count the number of vowels in string 
String= input('enter the string:')
count = 0
String=String.lower()
for i in String :
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count+=1
if count==0:
    print('no vowels found')
else:
    print('total vowels are:'+ str(count))