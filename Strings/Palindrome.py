def palindrome(a):
     c=list(a)
     l=len(c)
     le=l-1
     for i in range(l//2):
        temp=c[i]
        c[i]=c[le]
        c[le]=temp
        le-=1
     b="".join(c)
     print(b)
     if(a==b):
         print("It is a palindrome......")
     else:
         print("It is not a plaindrome.......")


b=''
a=input("Enter the String :")
palindrome(a)