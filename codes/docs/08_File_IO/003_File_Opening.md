# File Opening

# Open Function

## Syntax'

- You can open file using Python's built-in ` open()` function

```python 
file_object = open(file_name, [access_mode])
```

### Parameters

- `file_name`: The `file_name`argument is a string value that contains the name of the files that you want to access.
-`access_mode`: The `access_name` determines the mode in which the file to be opened, i.e.,
- read
- write
- append

### Open Function - AccessMode

- r: This is defaultmode. Opens a filefor reading only
- rb: Opens a file reading only in binary format
- r+: Opens a file for both reading and writing
- rb+: Opens a file for both reading and writing in binary formatting
- w: Opens a file for writing only
  -Overwrites the file if the file exists
  - creates a newfile for writing if the filedoesn'texist
- wb: Opens a file for writing only in binary format
   - Overwrites the file if the file exists
   - Create a new file for writing if the file doesn't exist