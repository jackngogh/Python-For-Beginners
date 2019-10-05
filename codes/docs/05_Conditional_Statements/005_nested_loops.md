# Nested Loops

## Definition:

- Nested loop basicallymeans a loop inside a loop
- It can be a For loop inside a while loop and vice versa
- It can also be a whileloop inside a while loop ora for loop inside a for loop

# Syntax

```python
count = 1
for i in range(10):
    print(str(i) *i)

    for j in range(0, i):
        count = count + 1
```

