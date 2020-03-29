
from collections import Counter
x='cars bikes arcs steer'
x=x.split(' ')

for i in range(0,len(x)):
    x[i]=''.join(sorted(x[i]))

    Dic=Counter(x)
print(max(Dic.values()))


