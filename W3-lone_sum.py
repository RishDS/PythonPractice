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
