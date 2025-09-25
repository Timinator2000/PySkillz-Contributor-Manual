# Hello, World! (3 Times)

Consider the following exercise: Print the following text:

```text
Hello, World!
Hello, World!
Hello, World!
```

@[How many solutions can you find?]({"stubs": ["exercises/hello_word_3x/hello_world_3x.py"], "command": "python3 exercises/hello_word_3x/hello_world_3x_test.py"})

Even a simple task like this can be solved in many different ways. Let’s look at several valid approaches. For each solution, we’ll analyze: 

* **Number of Calls to `print`** (during execution)

* **Lines of Code** (counting the function header and logical lines, but skipping blank lines)

* **Statements** (Python statements, including function definitions)

# Three Direct Print Calls

```python
def hello_word_3_times():
    print("Hello, World!")
    print("Hello, World!")
    print("Hello, World!")
```

* **Calls to `print`:** 3
* **Lines of code:** 4
* **Statements:** 4 (function definition, `print`, `print`, `print`)

# Multi-Line String

```python
message = '''

Hello, World!
Hello, World!
Hello, World!

'''.strip()

def hello_word_3_times():
    print(message)
```

* **Calls to `print`:** 1
* **Lines of code:** 7
* **Statements:** 3 (`message = ...`, function definition, `print(message)`)

# Using a `for` Loop

```python
def hello_word_3_times():
    for _ in range(3):
        print("Hello, World!")
```

* **Calls to `print`:** 3
* **Lines of code:** 3
* **Statements:** 3 (function definition, `for`, `print`)

# Using a `while` loop

```python
def hello_word_3_times():
    i = 0
    while i < 3:
        print("Hello, World!")
        i += 1
```

* **Calls to `print`:** 3
* **Lines of code:** 5
* **Statements:** 4 (function definition, `i=0`, `while`, `print`, `i+=1`)

# Joining a list

```python
def hello_word_3_times():
    print("\n".join(["Hello, World!"] * 3))
```

* **Calls to `print`:** 1
* **Lines of code:** 2
* **Statements:** 2 (function definition, `print`)

# Recursion

```python
def hello_word_3_times(n=3):
    if n > 0:
        print("Hello, World!")
        hello_word_3_times(n - 1)
```

* **Calls to `print`:** 3
* **Lines of code:** 4
* **Statements:** 4 (function definition, `if`, `print`, recursive call)

---

Even for a simple exercise, the variety of valid solutions shows how options like `strict_print_usage`, `max_lines_of_code` and `max_statement_count` could limit the number of accepted soltuions. These options can help you guide learners toward the style of solution you want to encourage.







# Overriding the `check_additonal_solution_criteria` Method

Look at all the possible soltutions above. Let's say the exercise asked the user to use a `while` loop. All `Exercise`s are, ultimately, subclasses a `TechioObject`. A `TechioObject` object only exists after a learner clicks on **Run** in a graded code block. During the object instantiation, a code analysis is run on the learner's code and saved in `self.code_analysis`, a dictionary with the following important keys:

| Key | Meaning |
|:---:|:--------|
| filename | learner's source code filename |
| source | learner's full source code |
| categories | list of (node, category, keep, depth) |
| total_count | number of statements |
| **kept** | `Counter` with keys being code constructs |
| skipped | `Counter` with keys being code constructs |
| total_lines | total lines in the the learner's source code |
| non_blank_lines | number of lines that are not blank |
| comment_lines | number of comment lines in the learner's code |
| effective_code_lines | lines of code = `non_blank_lines - comment_lines' |

You are free to use this information in any way to determine if the learner has met the exercise objectives. In the end, `check_additonal_solution_criteria` must return a string. An empty string indicates all additional criteria have been met. Any other string should be a message to be displayed to the learner explaining what additional criteria **has not** been met.

For instance, if the the exercise above was written as:

>Use a `while` loop to print the following:
>
>Hello, World!
>Hello, World!
>Hello, World!

By overriding the `check_additonal_solution_criteria` as shown below, you can you check to make sure the leaner used a `while` loop as compared to a `for` loop or simply `str.join`? If you find a `while` loop, return an empty string. Otherwise, return a message that may be sent to the user explaining why the submitted solution has failed.

```python
    def check_additonal_solution_criteria(self) -> str:
        if 'while' in self.code_analysis.kept:
            return ''

        return 'Your code must include a while loop to successfully complete this exercise.'
```


<BR>

************

[![PySkillz](../../graphics/PySkillzFooter.png)](skillz-catalog)
