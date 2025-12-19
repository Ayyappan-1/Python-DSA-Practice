# It just removes space and remains alphabets, numbers and symbols as it is...
def space_removal(a,b):
    for i in a:
        if(i.isspace()):
            pass
        else:
            b+=i
    return b

b=''
a=input("Enter the string :")
b=space_removal(a,b)
print(b)