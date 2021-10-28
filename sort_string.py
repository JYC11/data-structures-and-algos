import re

string = input()

nums = str(sum(list(map(int,re.findall("\d",string)))))
string = ''.join(sorted(re.sub("\d","",string)))

print(string+nums)