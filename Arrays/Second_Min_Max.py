def second_min_max(a):
    l=len(a)
    b=sorted(a)
    return b[1], b[l-2]

a=[1,4,2,6,7,0,9]
minimum,maximum=second_min_max(a)
print(f"The second smallest number is :{minimum}\nThe seond largest number is :{maximum}")
