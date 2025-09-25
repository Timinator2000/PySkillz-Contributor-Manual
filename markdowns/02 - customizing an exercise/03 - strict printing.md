# Strict Printing

```python
class HelloWorld3XStrictPrinting(pyskillz_tools.PrintBasedExercise):
    
    def __init__(self):

        super().__init__(__file__)
        self.fixed_test_cases = [[]]

        self.strict_printing = True
```




Use a multi-line string to print the following text:

```text
Hello, World!
Hello, World!
Hello, World!
```

@[Make sure you only call print a single time!]({"stubs": ["exercises/hello_world_3x_strict_printing/hello_world_3x_strict_printing.py"], "command": "python3 exercises/hello_world_3x_strict_printing/hello_world_3x_strict_printing_test.py"})
