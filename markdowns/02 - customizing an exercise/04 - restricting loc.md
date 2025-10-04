# Restricted Lines of Code

When you want to **limit the number of lines** a learner can write, use the `max_lines_of_code` attribute. This can be useful for encouraging concise solutions, discouraging unnecessary boilerplate, or guiding learners toward specific patterns.

To enable this restriction, set the `max_lines_of_code` attribute to the maximum number of allowed lines in your subclass constructor, as shown below.


```python
class HelloWorld3XRestrictedLOC(pyskillz_tools.PrintBasedExercise):
    
    def __init__(self):

        super().__init__(__file__)
        self.fixed_test_cases = [[]]

        self.max_lines_of_code = 1
```


Print the following text using **only 1 line of code**.

```text
Hello, World!
Hello, World!
Hello, World!
```

Write your own solution or try any one of the solutions provided earlier.

@[Only one line of code...]({"stubs": ["exercises/hello_world_3x_restricted_loc/hello_world_3x_restricted_loc.py"], "command": "python3 exercises/hello_world_3x_restricted_loc/hello_world_3x_restricted_loc_test.py"})


# Results

1️⃣ ❌ Three Direct Print Calls

2️⃣ ❌ Multi-Line String

3️⃣ ❌ Using a `for` Loop

4️⃣ ❌ Using a `while` Loop

5️⃣ ❌ Joining a List

6️⃣ ✅ One-Liner with String Multiplication

7️⃣ ✅ One-Liner with 3 Print Statements

8️⃣ ❌ Recursion

<BR>

************

[![PySkillz](../../graphics/PySkillzFooter.png)](skillz-catalog)
