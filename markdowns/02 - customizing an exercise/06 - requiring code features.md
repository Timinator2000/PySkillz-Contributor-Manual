# Overriding the `check_additional_solution_criteria` Method

After the learner’s `print` usage, lines of code, and number of Python statements have all passed their respective checks, one final step is performed: the `check_additional_solution_criteria` method is called.

This method provides your **most flexible opportunity** to customize an `Exercise`. By default, it simply returns an empty string, indicating that no additional errors were found. You can override this method to implement any kind of custom solution checking you need.

Importantly, this method runs **only if all earlier checks pass**. If the learner’s submission fails a print usage, line count, or statement count check, `check_additional_solution_criteria` is not called.

# Return Values

Your override should return:

* An **empty string** (`''`) if no additional errors are found.
* A **non-empty string** describing the error if the learner’s code fails your custom check.

# `code_analysis`: an Attribute of Every `TechioObject`

All `Exercise`s are ultimately subclasses of `TechioObject`. A `TechioObject` object is created **only after** the learner clicks **Run** in a graded code block. During this instantiation, the learner’s code is analyzed and stored in `self.code_analysis`, a dictionary with several useful keys:

|            Key           | Meaning                                                             |
| :----------------------: | :------------------------------------------------------------------ |
|       `'filename'`       | Learner's source code filename                                      |
|       **`'tree'`**       | **Learner's code parsed into an Abstract Syntax Tree (AST)**        |
|        `'source'`        | Learner's full source code                                          |
|      `'categories'`      | List of `(node, category, keep, depth)` tuples                      |
|      `'total_count'`     | Number of statements                                                |
|         `'kept'`         | `Counter` of code constructs that were counted                      |
|        `'skipped'`       | `Counter` of code constructs that were skipped                      |
|      `'total_lines'`     | Total lines in the learner's source code                            |
|    `'non_blank_lines'`   | Number of non-blank lines                                           |
|     `'comment_lines'`    | Number of comment lines                                             |
| `'effective_code_lines'` | Lines of code excluding comments: `non_blank_lines - comment_lines` |

You can use any of this information to determine whether the learner has met your exercise objectives. However, **the Abstract Syntax Tree (AST) is often the most powerful tool** for writing meaningful checks.

To access it:

```python
tree = self.code_analysis['tree']
```

---

# Abstract Syntax Tree (AST)

The **Abstract Syntax Tree (AST)** is a structured representation of the learner’s code. Instead of analyzing raw strings, you can traverse the AST to understand exactly **what constructs** the learner used — such as loops, functions, or conditionals.

For example, to check whether the learner used a `for` loop:

```python
    def check_additional_solution_criteria(self):
        tree = self.code_analysis['tree']

        for node in ast.walk(tree):
            if isinstance(node, ast.For):
                return ''
        
        return 'Your solution must include a \'for\' loop.'
```

Other useful node types include `ast.While`, `ast.FunctionDef`, `ast.Call`, `ast.If`, and `ast.Return`.

The AST provides a language-aware way to build deeper, more precise checks than simple text analysis. **If you plan to write complex custom criteria, it’s strongly recommended that you explore the power of ASTs further using your favorite AI tool** — ask it to explain node types, write detection examples, or help debug traversal logic.

# An Example

Use a `while` loop to print the following text:

```text
Hello, World!
Hello, World!
Hello, World!
```

The following subclass enforces the use of a `while` loop:

```python
import ast

class HelloWorld3XWithAWhileLoop(pyskillz_tools.PrintBasedExercise):
    
    def __init__(self):

        super().__init__(__file__)
        self.fixed_test_cases = [[]]

    
    def check_additional_solution_criteria(self):
        tree = self.code_analysis['tree']

        for node in ast.walk(tree):
            if isinstance(node, ast.While):
                return ''
        
        return 'Your solution must include a \'while\' loop.'
```

Write your own solution or try any one of the solutions provided earlierl

@[Hello World 3 Times with a `while` Loop.]({"stubs": ["exercises/hello_world_3x_with_a_while_loop/hello_world_3x_with_a_while_loop.py"], "command": "python3 exercises/hello_world_3x_with_a_while_loop/hello_world_3x_with_a_while_loop_test.py"})


# Results

1️⃣ ❌ Three Direct Print Calls

2️⃣ ❌ Multi-Line String

3️⃣ ❌ Using a `for` Loop

4️⃣ ✅ Using a `while` Loop

5️⃣ ❌ Joining a List

6️⃣ ❌ One-Liner with String Multiplication

7️⃣ ❌ One-Liner with 3 Print Statements

8️⃣ ❌ Recursion

<BR>

************

[![PySkillz](../../graphics/PySkillzFooter.png)](skillz-catalog)
