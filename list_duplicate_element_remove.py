test_list =[1,2,3,2,4,5,1,6,2,9,8]
print ( str(test_list)) 

  
  
a = [] 
for x in test_list:
    if x not in a:
        a.append(x)
    else:
        x='N'
        a.append(x)
  
# printing list after removal  
print ( str(a))
