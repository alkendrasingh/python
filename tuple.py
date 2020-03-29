test_list=[(4,5),(6,1),(3,6),(4,3),(5,2),(2,5),(1,6)]
print(str(test_list))

'''for i in range(len(test_list)):
    
     test_list[i]=sum(test_list[i])
         
     
     print(test_list[i])'''

l=[]  
        
for i in test_list:
    if i[0]+i[1]==7:
        l.append(i)

print(str(l))
