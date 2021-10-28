import sys
from collections import deque
sentence = list(sys.stdin.readline().strip())
# sentence = [i for i in '<   space   >space space space<    spa   c e>']

final = ''
tag = deque() #deque
word = [] #stack
add_tag = False
for i in sentence:
    if i == "<":
        tag.append(i)
        while word:
            final += word.pop()
        add_tag = True
    elif i == ">":
        tag.append(">")
        while tag:
            final += tag.popleft()
        add_tag = False
    elif i == ' ':
        while word:
            final += word.pop()
        if add_tag == True:
            tag.append(i)
        else:
            final += i
    else:
        if add_tag == True:
            tag.append(i)
        else:
            word.append(i)
print(final + ''.join(word[::-1]))    

"""
<abc>efg hij<klm>

<
<a
<ab
<abc
<abc> = append
> found so append

e
ef
efg
efg\s = reverse append
\s so reverse append

' ' = just append

h
hi
hij
hij< = reverse append



if <

elif >

elif  ' '

else



"""