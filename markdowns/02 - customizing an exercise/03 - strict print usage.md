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

Write your own solution or try any one of the solutions provided earlier

@[To pass successfully, you must only call print one time!]({"stubs": ["exercises/hello_world_3x_strict_print_usage/hello_world_3x_strict_print_usage.py"], "command": "python3 exercises/hello_world_3x_strict_print_usage/hello_world_3x_strict_print_usage_test.py"})
