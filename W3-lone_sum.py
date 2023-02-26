'''
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.


lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
'''

def lone_sum(a, b, c):
  if a==b==c:
    return 0
  if a==b:
    return c
  if b==c:
    return a
  if c==a:
    return b
  return a+b+c

#or

def lone_sum(a, b, c):
    values = [a,b,c]
    unique_values = {a, b, c}
    if len(unique_values) == 3:
        return a + b + c
    for i in values:
       if values.count(i)==1:
          return i
    return 0
  
#or

def lone_sum(a, b, c):
  sum = 0
  if a != b and a != c: sum += a
  if b != a and b != c: sum += b
  if c != a and c != b: sum += c
  
  return sum

'''
Both programs have the same time complexity of O(1) because they always execute a constant number of comparisons and returns a result.
However, the second program has a slightly higher space complexity of O(n) because it creates a list to store the input values.
The second program also has an additional loop to count the occurrence of each value in the input list.
This loop is only executed if there are duplicates in the input list.
In the worst case, if all the input values are the same, the loop will execute three times, so the time complexity of the second program is still O(1).
Overall, both programs have similar time complexities and will have similar performance for small input sizes.
However, the first program is more concise and easier to read, while the second program has more explicit logic and may be more appropriate 
for larger and more complex programs.
The third program is the most concise and has the lowest space complexity. 
'''
