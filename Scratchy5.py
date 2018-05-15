not_having_duplicates=set()
having_duplicates=set()
string='aabcb'
for i in string:
    if i in having_duplicates:
        continue        
    else:
        if i in not_having_duplicates:
            not_having_duplicates.remove(i)
            having_duplicates.add(i)    
        else:
            not_having_duplicates.add(i)
print(not_having_duplicates,having_duplicates,sep='\n')                
