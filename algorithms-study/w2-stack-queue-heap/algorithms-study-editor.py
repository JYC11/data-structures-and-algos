import sys

stack1 = list(sys.stdin.readline().strip())
N = int(sys.stdin.readline())
stack2 = []

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'P':
        stack1.append(command[1])
    if command[0] == 'L' and stack1 != []:
        stack2.append(stack1.pop())
    if command[0] == 'D' and stack2 != []:
        stack1.append(stack2.pop())
    if command[0] == 'B' and stack1 != []:
        stack1.pop()

print(''.join(stack1+stack2[::-1]))

"""
          s1                s2
      [a,b,c,d]cursor        []
P x   [a,b,c,d,x]cursor       []
L     [a,b,c,d]cursor        [x]
P y   [a,b,c,d,y]cursor      [x]
D     [a,b,c,d,y,x]cursor    []
B     [a,b,c,d,y]
"""