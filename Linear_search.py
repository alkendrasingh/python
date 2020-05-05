l=[2,3,5,4,7,6,8,9]

search_for=8

result=-1
for i in range(len(l)):
    if search_for == l[i]:
        result = i
        break

print(result)
