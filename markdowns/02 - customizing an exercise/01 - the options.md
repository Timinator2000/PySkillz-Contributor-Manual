# Customizing an Exercise

Most exercises will work fine without customization, but sometimes you need extra precision in how the learner’s code is evaluated. The `Exercise` class provides several options and extension points that let you do this.

# Built-in Options

* **`strict_print_usage`** (only used with a `PrintBasedExercise`)
  Requires the learner to use the `print` function the same number of times as the grader. This ensures they follow the intended output pattern instead of, for example, concatenating everything into a single `print` call.

* **`max_statement_count`**
  Places an upper bound on the total number of Python statements in the learner’s solution. This is helpful if you want to discourage brute-force or repetitive solutions.

* **`max_lines_of_code`**
  Places an upper bound on the number of lines of code. While similar to `max_statement_count`, this option focuses on formatting and conciseness rather than just logical statements.

* **`floating_point_precision`**
  Controls how floating point values are compared between the grader and the learner. Answers are rounded to this number of decimal places before comparison. The default is `2`, which usually provides a good balance between precision and flexibility.

# Overridable Methods

If the built-in options aren’t enough, your exercise subclass can override one or both of the following methods:

* **`test_case_to_string`**
  Determines how a test case is displayed to the learner. In most cases, the default behavior is sufficient—it lists each parameter with its value. Only override this if you need a custom presentation.

* **`check_additional_solution_criteria`**
  Lets you add custom checks on the learner’s code beyond correctness. For instance, you could confirm that the solution includes at least one `for` loop, avoids certain functions, or uses recursion.

# Next Steps

Now that we’ve seen the different customization options available, let’s look at them in action. We’ll start with a very simple problem — printing “Hello, World!” three times. Even for a task this basic, learners can solve it in many different ways, and you may decide to customize your exercise to encourage or require a particular style of solution.




# I'M NOT SURE THIS WILL BE USED:

1) Compare user solution to grader solution.

  * if `strict_print_usage` = `True`, more checking is done.

2) If all test cases pass #1, check `statement_count` vs `max_statement_count`

3) If code passes #2, check `lines_of_code` vs `max_lines_of_code`

4) If code passes #3, check any additional grader criteria by calling `check_additonal_solution_criteria` method.

<BR>

************

[![PySkillz](../../graphics/PySkillzFooter.png)](skillz-catalog)
