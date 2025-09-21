# Hello World 3 Times

Consider the following exercise: Print the following text:

```text
Hello, World!
Hello, World!
Hello, World!
```

Assume the learner is given the following code stub:

```python
def hello_word_3_times():
    # Your code goes here.
```

How many different solutions could you write? Probably a bunch! Let’s look at several different ways to code a solution. For each solution, we’ll analyze:

* **Number of calls to `print`** (during execution)
* **Number of lines of code** (function header + code, but no blank lines or comment lines)
* **Number of Python statements** (measured by parsing the code)

---

# Solution 1: Three direct print calls

```python
def hello_word_3_times():
    print("Hello, World!")
    print("Hello, World!")
    print("Hello, World!")
```

* **Calls to `print`:** 3
* **Lines of code:** 4
* **Statements:** 3

---

# Solution 2: Using a `for` loop

```python
def hello_word_3_times():
    for _ in range(3):
        print("Hello, World!")
```

* **Calls to `print`:** 3
* **Lines of code:** 3
* **Statements:** 2 (`for` loop, `print`)

---

# Solution 3: Using a `while` loop

```python
def hello_word_3_times():
    i = 0
    while i < 3:
        print("Hello, World!")
        i += 1
```

* **Calls to `print`:** 3
* **Lines of code:** 5
* **Statements:** 4 (`i=0`, `while`, `print`, `i+=1`)

---

### Solution 4: String multiplication with newline

```python
def hello_word_3_times():
    print("Hello, World!\n" * 3, end="")
```

* **Calls to `print`:** 1
* **Lines of code:** 2
* **Statements:** 1

---

### Solution 5: Joining a list

```python
def hello_word_3_times():
    print("\n".join(["Hello, World!"] * 3))
```

* **Calls to `print`:** 1
* **Lines of code:** 2
* **Statements:** 1

---

### Solution 6: Recursion

```python
def hello_word_3_times(n=3):
    if n > 0:
        print("Hello, World!")
        hello_word_3_times(n - 1)
```

* **Calls to `print`:** 3
* **Lines of code:** 4
* **Statements:** 3 (`if`, `print`, recursive call)

---

### Solution 7: Assign a reference to `print`

```python
def hello_word_3_times():
    p = print
    p("Hello, World!")
    p("Hello, World!")
    p("Hello, World!")
```

* **Calls to `print`:** 3
* **Lines of code:** 5
* **Statements:** 4

---

### Solution 8: Loop over a list of values

```python
def hello_word_3_times():
    for _ in ["a", "b", "c"]:
        print("Hello, World!")
```

* **Calls to `print`:** 3
* **Lines of code:** 3
* **Statements:** 2

---

### Solution 9: Map with a throwaway function

```python
def hello_word_3_times():
    list(map(lambda _: print("Hello, World!"), range(3)))
```

* **Calls to `print`:** 3
* **Lines of code:** 2
* **Statements:** 1

---

### Solution 10: Comprehension with side effect

```python
def hello_word_3_times():
    [print("Hello, World!") for _ in range(3)]
```

* **Calls to `print`:** 3
* **Lines of code:** 2
* **Statements:** 1

---

Even for a simple exercise like printing three lines, the number of `print` calls, lines of code, and statements can vary a lot depending on the learner’s approach. This variety is exactly why the customization options (`strict_print_usage`, `max_statement_count`, etc.) are so useful—they let you tune the grader to emphasize the style of solution you want learners to produce.

---

Do you want me to **add a table summary** at the end (one row per solution, with the three metrics) so contributors can quickly compare all approaches side by side?







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
