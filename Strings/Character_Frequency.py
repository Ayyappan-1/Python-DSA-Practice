def sample(a):
    alphabet={}
    for i in a:
        if(i.isspace()==False):
            if(i not in alphabet):
               alphabet.update({i:1})
            else:
               alphabet[i]+=1
    for keys in alphabet.keys():
        print(f"Alphabet {keys} is repeated : {alphabet.get(keys)}")

a=input("Enter the number :")
sample(a)