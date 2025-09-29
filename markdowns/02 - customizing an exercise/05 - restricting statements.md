# Restricted Python Statement Count


```python
class HelloWorld3XRestrictedStatements(pyskillz_tools.PrintBasedExercise):
    
    def __init__(self):

        super().__init__(__file__)
        self.fixed_test_cases = [[]]

        self.max_statement_count = 2
```


Print the following text using no more than 2 Python statements.

```text
Hello, World!
Hello, World!
Hello, World!
```

Write your own solution or try any one of the solutions provided earlier

@[No more than 2 Python statements...]({"stubs": ["exercises/hello_world_3x_restricted_statements/hello_world_3x_restricted_statements.py"], "command": "python3 exercises/hello_world_3x_restricted_statements/hello_world_3x_restricted_statements_test.py"})


# Results

1️⃣ ❌ Three Direct Print Calls

2️⃣ ❌ Multi-Line String

3️⃣ ❌ Using a `for` Loop

4️⃣ ❌ Using a `while` Loop

5️⃣ ✅ Joining a List

6️⃣ ✅ One-Liner with String Multiplication

7️⃣ ❌ One-Liner with 3 Print Statements

8️⃣ ❌ Recursion
