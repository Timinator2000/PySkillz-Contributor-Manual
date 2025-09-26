# Restricted Lines of Code

Let's restric the user to 1 line of code:

```python
class HelloWorld3XRestrictedLOC(pyskillz_tools.PrintBasedExercise):
    
    def __init__(self):

        super().__init__(__file__)
        self.fixed_test_cases = [[]]

        self.max_lines_of_code = 1
```


Print the following text using 2 lines of code or less.

```text
Hello, World!
Hello, World!
Hello, World!
```

@[Only one line of code...]({"stubs": ["exercises/hello_world_3x_restricted_loc/hello_world_3x_restricted_loc.py"], "command": "python3 exercises/hello_world_3x_restricted_loc/hello_world_3x_restricted_loc_test.py"})


