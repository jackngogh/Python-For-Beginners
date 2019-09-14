# Membership Operator

## `in`

- Evaluate TRUW if it finds a variable in the specified sequence and FALSE otherwise

## `not in`

- Evaluates to TRUE if it does not finds a variable in the specified sequence and FALSE otherwise

## Examples

```shellType "help", "copyright", "credits" or "license" for more information. >>> list = (4, 5, 6)
>>> print(list)
(4, 5, 6)
>>> print(4 not in list)
False
>>> print(100 is in list)
  File "<stdin>", line 1
    print(100 is in list)
                  ^
SyntaxError: invalid syntax
>>> print(100 in list)
False
>>> A = [3, 45, 6, "Jack"]
>>> A
[3, 45, 6, 'Jack']
>>> print(100 in A)
False
>>> print("Jack" in A)
True
>>> print("jack" in A)
False
>>> exit()
```