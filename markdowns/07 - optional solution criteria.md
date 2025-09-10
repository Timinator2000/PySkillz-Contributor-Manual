# The Grading Process

1) Compare user solution to grader solution.

  * if `strict_print_usage` = `True`, more checking is done.

2) If all test cases pass #1, check `statement_count` vs `max_statement_count`

3) If code passes #2, check `lines_of_code` vs `max_lines_of_code`

4) If code passes #3, check any additional grader criteria by calling `additonal_solution_criteria` method.


# The Options

`strict_print_usage`
`max_statement_count`
`max_lines_of_code`

Additionally, you may add any criteria you wish by overriding the the `additonal_solution_criteria` method.

# Examples

Consider the following exercise: Print the following text:

```text
Hello, World!
Hello, World!
Hello, World!
```

Assume the user is given the following code stub:

```python
def hello_word_3_times():
    # Your code goes here.
```

Now, let's look at a bunch of different ways to code a solution. For each solution, I'll do an analysis and determine the number of calls to `print` when the code executes, the number of lines of code and the number of statements in the solution.


# Overriding the `additonal_solution_criteria` Method

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

You are free to use this information in any way to determine if the learner has met the exercise objectives. In the end, `additonal_solution_criteria` must return a string. An empty string indicates all additional criteria have been met. Any other string should be a message to be displayed to the learner explaining what additional criteria **has not** been met.

For instance, if the the exercise above was written as:

>Use a `while` loop to print the following:
>
>Hello, World!
>Hello, World!
>Hello, World!

By overriding the `additonal_solution_criteria` as shown below, you can you check to make sure the leaner used a `while` loop as compared to a `for` loop or simply `str.join`? If you find a `while` loop, return an empty string. Otherwise, return a message that may be sent to the user explaining why the submitted solution has failed.

```python
    def check_additonal_solution_criteria(self) -> str:
        if 'while' in self.code_analysis.kept:
            return ''

        return 'Your code must include a while loop to successfully complete this exercise.'
```