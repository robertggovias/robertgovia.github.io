from collections import deque

my_deque = deque('abcde') # New deque with 5 items

# Print them one at a time as they are popped off the stack
"""
for i in range(len(my_deque)):
  print(my_deque.pop())
"""
#However, this seems a natural place for a while loop#

# Print them one at a time as they are popped off the stack

while my_deque:
  print(my_deque.pop())
