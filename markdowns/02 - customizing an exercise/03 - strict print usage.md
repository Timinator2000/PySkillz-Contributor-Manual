# Strict Print Usage

```python
class HelloWorld3XStrictPrintUsage(pyskillz_tools.PrintBasedExercise):
    
    def __init__(self):

        super().__init__(__file__)
        self.fixed_test_cases = [[]]

        self.strict_print_usage = True
```


Use a multi-line string to print the following text:

```text
Hello, World!
Hello, World!
Hello, World!
```

@[Make sure you only call print a single time!]({"stubs": ["exercises/hello_world_3x_strict_print_usage/hello_world_3x_strict_print_usage.py"], "command": "python3 exercises/hello_world_3x_strict_print_usage/hello_world_3x_strict_print_usage_test.py"})
