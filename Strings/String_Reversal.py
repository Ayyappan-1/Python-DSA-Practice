# String Reversal by using simple concatination technique 
def reversal(a):
    global b
    b=""
    for i in range(len(a)-1,-1,-1):
      b+=a[i]

# Using list converstion technique to reverse a string and return it in string type
def Optimized(a):
   a=list(a)
   l=len(a)
   le=l-1
   for i in range(l//2):
      temp=a[i]
      a[i]=a[le]
      a[le]=temp
      le-=1
   return "".join(a)
    
a=input("Enter a String :")
s=''
reversal(a)
print("Concatenation Method :",b)
s=Optimized(a)
print("List Reversal Method :",s)
 