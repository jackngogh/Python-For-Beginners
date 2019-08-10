# Mutable Data Types


- Lists
- Dictionaries
- Sets

## Lists

- List is an ordered set of elements enclosed wit square brackets

### Main Diffference between lists and tuples

- Lists are enclosed in brackets[]while tuples are enclosed within praenthesis()
- Lists are Mutable and tuples are immutable
- Tuples are faster than lists

```python
A = [1, 2, 3.15, 'Education']
print(A)
```

## Dictionaries

### Definitions

- Dictionaries contain key value pairs
- Each key is seperated from itsvalue by a colon '(:)'
- The items are seperated by comma
- The whole thing is enclosed within a curly bracket

### Example

- keys: 'Age', 'Name'
- values: 24, 'John'

```python
A = {'Age': 24, 'Name': 'John'}
```

## Sets

### Definitions

- A set is an unodered collection of items
- Every eleent is unique
- A set is created by placing all the items(elements) inside curly brackets '{}', seperated by comma

### Example

```python
A = {1, 2, 3, 3}

print(A)
```

Output: 

```shell
{1, 2, 3}
```