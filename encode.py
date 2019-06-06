str1=input()
str2=input()
str3=''
for i in range(0,len(str1)):
    num1=(ord(str1[i]))-96
    num2=(ord(str2[i]))-96
    if((num1+num2)<=26):
        str3=str3+(chr(96+num1+num2))
    else:
        str3=str3+(chr(96+(num1+num2-26)))
print(str3)        
