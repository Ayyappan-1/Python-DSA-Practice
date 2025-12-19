def counting(a):
    v,c=0,0
    vowel={'a','i','e','o','u'}
    for i in a:
        if(i.lower() in vowel):
            v+=1
        elif(i.isalpha()):
            c+=1
    print(f"Number of Vowels in String : {v}\nNumber of Consonants in String : {c}")


print()
a=input("Enter the Sentence :")
counting(a)
