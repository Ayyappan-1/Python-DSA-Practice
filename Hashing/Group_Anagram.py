# Anagram grouping by using hash mapping which has the time complexity of O(n* K log K) and space complexity of O(n * K)
def anagram_grouping(a):
    anagram_group={}
    for i in a:
        i_sort=sorted(i)
        i_sort="".join(i_sort)
        if(i_sort not in anagram_group):
            anagram_group[i_sort]=[i]
        else:
            anagram_group[i_sort].append(i)
    return anagram_group

a=["ate","eat","tea","ayya","ayay"] 
anagram=anagram_grouping(a)
print(anagram) 