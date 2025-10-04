# Strict Print Usage

When *strict print usage* is required, the learner’s solution must call `print` exactly the same number of times as the grader. This ensures that learners follow the intended output structure rather than merging multiple outputs or adding extras.

The simplest case is when the grader uses a single `print` statement, but you can also use this feature to enforce more complex output patterns.

To enable this behavior in your exercise, set the `strict_print_usage` attribute to `True` in your subclass constructor, as shown below.


```python
class HelloWorld3XStrictPrintUsage(pyskillz_tools.PrintBasedExercise):
    
    def __init__(self):

        super().__init__(__file__)
        self.fixed_test_cases = [[]]

        self.strict_print_usage = True
```

Use a multi-line string or another technique to print the following text with **only 1 call to `print`**:

```text
Hello, World!
Hello, World!
Hello, World!
```

Write your own solution or try any one of the solutions provided earlier.

@[To pass successfully, you must only call print one time!]({"stubs": ["exercises/hello_world_3x_strict_print_usage/hello_world_3x_strict_print_usage.py"], "command": "python3 exercises/hello_world_3x_strict_print_usage/hello_world_3x_strict_print_usage_test.py"})

# Results

1️⃣ ❌ Three Direct Print Calls

2️⃣ ✅ Multi-Line String

3️⃣ ❌ Using a `for` Loop

4️⃣ ❌ Using a `while` Loop

5️⃣ ✅ Joining a List

6️⃣ ✅ One-Liner with String Multiplication

7️⃣ ❌ One-Liner with 3 Print Statements

8️⃣ ❌ Recursion

<BR>

************

[![PySkillz](../../graphics/PySkillzFooter.png)](skillz-catalog)
