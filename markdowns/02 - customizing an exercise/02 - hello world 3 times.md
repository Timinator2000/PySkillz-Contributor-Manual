# Hello, World! (3 Times)

Consider the following exercise: 

Print the following text:

```text
Hello, World!
Hello, World!
Hello, World!
```

@[How many different solutions can you code?]({"stubs": ["exercises/hello_world_3x/hello_world_3x.py"], "command": "python3 exercises/hello_world_3x/hello_world_3x_test.py"})

Even a simple task like this can be solved in many different ways. Let’s look at several valid approaches. For each solution, we’ll analyze: 

* **Number of Calls to `print`** (during execution)

* **Lines of Code** (counting the function header and code lines, but skipping blank lines)

* **Statements** (Python statements, including function definitions)

> 🤔 For a more detailed discussion of how PySkillz counts lines of code and Python statements, see [Appendix A - Counting Lines of Code]() on the main PySkillz playground.

**LINK NEEDED**

# 1️⃣ Three Direct Print Calls

```python
def hello_world_3x() -> None:
    print("Hello, World!")
    print("Hello, World!")
    print("Hello, World!")
```

* **Calls to `print`:** 3
* **Lines of code:** 4
* **Statements:** 4 (`hello_world_3x()`, `print`, `print`, `print`)

# 2️⃣ Multi-Line String

```python
message = '''

Hello, World!
Hello, World!
Hello, World!

'''.strip()

def hello_world_3x() -> None:
    print(message)
```

* **Calls to `print`:** 1
* **Lines of code:** 7
* **Statements:** 3 (`message = ...`, `hello_world_3x()`, `print(message)`)

# 3️⃣ Using a `for` Loop

```python
def hello_world_3x() -> None:
    for _ in range(3):
        print("Hello, World!")
```

* **Calls to `print`:** 3
* **Lines of code:** 3
* **Statements:** 3 (`hello_world_3x()`, `for`, `print`)

# 4️⃣ Using a `while` Loop

```python
def hello_world_3x() -> None:
    i = 0
    while i < 3:
        print("Hello, World!")
        i += 1
```

* **Calls to `print`:** 3
* **Lines of code:** 5
* **Statements:** 5 (`hello_world_3x()`, `i=0`, `while`, `print`, `i+=1`)

# 5️⃣ Joining a List

```python
def hello_world_3x() -> None:
    print("\n".join(["Hello, World!"] * 3))
```

* **Calls to `print`:** 1
* **Lines of code:** 2
* **Statements:** 2 (`hello_world_3x()`, `print`)


# 6️⃣ One-Liner with String Multiplication

```python
def hello_world_3x() -> None: print(("Hello, World!\n" * 3)[:-1])
```

* **Calls to `print`:** 1
* **Lines of code:** 1
* **Statements:** 2 (`hello_world_3x()`, `print`)

# 7️⃣ One-Liner with 3 Print Statements

```python
def hello_world_3x() -> None: print('Hello, World!'); print('Hello, World!'); print('Hello, World!')
```

# 8️⃣ Recursion

```python
def hello_world_3x(n=3) -> None:
    if n > 0:
        print("Hello, World!")
        hello_world_3x(n - 1)
```

* **Calls to `print`:** 3
* **Lines of code:** 4
* **Statements:** 4 (`hello_world_3x()`, `if`, `print`, recursive call)

# Summary

Even for a simple exercise, the variety of valid solutions shows how options like `strict_print_usage`, `max_lines_of_code` and `max_statement_count` could limit the number of accepted soltuions. These options can help you guide learners toward the style of solution you want to encourage. Let's put the results in a table and then take a look at ways to limit the number of solutions accepted as correct.

| | Technique | Calls to Print | Lines of Code | Python Statements |
|:--:|:-----------------:|:---:|:---:|:---:|
| 1️⃣ | Three Direct Print Calls | 3 | 4 | 4 |
| 2️⃣ | Multi-Line String | 1 | 7 | 3 |
| 3️⃣ | Using a `for` Loop | 3 | 3 | 3 |
| 4️⃣ | Using a `while` Loop | 3 | 5 | 5 |
| 5️⃣ | Joining a List | 1 | 2 | 2 |
| 6️⃣ | One-Liner with String Multiplication | 1 | 1 | 2 |
| 7️⃣ | One-Liner with 3 Print Statements | 3 | 1 | 4 |
| 8️⃣ | Recursion | 3 | 4 | 4 |

<BR>

************

[![PySkillz](../../graphics/PySkillzFooter.png)](skillz-catalog)
