# Step 5: The Python Files

To create a new exercise, three Python files need your attention:

* `exercise_name.py`
  * The __starter code__ presented to the learner.
  * Learners will edit this file to solve the exercise.

* `exercise_name_solution.py`
  * Your __working solution__ to the exercise.
    * The grader uses this file to determine the expected output.
    * After the learner successfully completes the exercise, this entire file is displayed as the suggested solution.
  
* `exercise_name_test.py`
  * The __exercise subclass__ that defines the specifics of this exercise, including:
    *  Static test cases for validation.
    *  The algorithm used to generate any random test cases.
    *  A success message displayed after the learner completes the exercise.

Let’s now take a closer look at the contents of each file so you know __exactly what to edit__ to get your new exercise up and running.

# exercise_name.py

The contents of this file are shown to the user in the code window. Keep it very short.

For exercises that have input parameters and return values (`pyskillz_tools.Exercise`), provide only a minimal function stub.

```python
def exercise_name(a: int, b: int) -> int:
    return # Your code goes here.
```

For exercises that take input and require the user to print an answer (`pyskillz_tools.PrintBasedExercise`), include a few extra comment lines.
Since all `print` output is graded, remind users they can use `sys.stderr` for debug messages.

```python
def exercise_name(a: int, b: int) -> None:
    # Your code goes here.
    
    # Write an answer using print
    # To debug: import sys at the top of this script
    #           print("Debug messages...", file=sys.stderr, flush=True)
```

# exercise_name_solution.py

This file contains the suggested solution along with any alternates. The primary solution is used by the grader to check correctness. Once the user completes the exercise successfully, the full contents of this file are displayed.

For `pyskillz_tools.Exercise`:

```python
def exercise_name(a: int, b: int) -> int:
    return a + b
```

For `pyskillz_tools.PrintBasedExercise`:

```python
def exercise_name(a: int, b: int) -> None:
    print(a + b)
```

# exercise_name_test.py

This file contains the main exercise logic. Define your exercise subclass, create an instance of it, and run the exercise.

The first section is reserved for setup and __must not be modified__. It imports the exercise framework from `pyskillz_tools.py`, the user’s solution from `exercise_name.py`, and the suggested solution from `exercise_name_solution.py`.

```python
###############################################################################################################
# Environment Setup - Do not change anything in this section.
###############################################################################################################

import os
import sys
import random

# Normalize path for current OS and split the path into directory and filename
dir_path, filename = os.path.split(os.path.normpath(__file__))

# Add tools directory to the OS PATH
sys.path.insert(0, os.path.join(dir_path, '..', '..', '----tools----'))

try:
    import pyskillz_tools
    pyskillz_tools.check_for_tech_io(dir_path)

except ImportError:
    print(f'Import Error: pyskillz_tools.py needs to be in the tools folder, one level deep from python-project.')

exercise_name = filename[:filename.find('_test.py')]
solution_filename = os.path.join(dir_path, f'{exercise_name}_solution.py')

exec(f'from {exercise_name} import {exercise_name} as user_solution')
exec(f'from {exercise_name}_solution import {exercise_name} as suggested_solution')

###############################################################################################################
# End Setup
###############################################################################################################
```

Next, define the message shown to the user when the exercise is completed successfully. Place this definition outside the class for easier formatting. A multiline string can be used to include elements like bullet points or even a short Q&A (e.g., a joke).

For paragraphs that require automatic word wrapping, break the text into separate lines and concatenate them. This keeps the text easy to read in the code while still displaying correctly to the user.

```python
success_message = """


"""

success_message += ''
success_message += ''
success_message += ''
```

Next, declare your exercise class by choosing one of the following lines. Each option specifies the exercise type your class will inherit from. Be sure to replace `ExerciseName` with the actual name of your exercise, matching the `exercise_name` wording used for your files.

```python
class ExerciseName(pyskillz_tools.Exercise):
class ExerciseName(pyskillz_tools.PrintBasedExercise):
```

The first line of the class constructor (`__init__` ) must remain unchanged. It calls the superclass constructor, passing in the user solution, the suggested solution, the suggested solution filename and the success message.

On the second line, specify the number of random test cases your exercise should generate. Random test cases are not required but are highly encouraged — they are simple to create and add robustness to the testing strategy.

Next, define a list of fixed test cases. Each test case is itself a list of arguments. The stub code below includes 5 empty test cases as placeholders, but you may use more or less. Insert arguments into each test case placeholder.

Remember: every test case must be a list of arguments, even if there is only one. For example:

* A single integer argument → `[5]`

* A list of integers as the lone argument → `[[1, 2, 3]]`

```python
    def __init__(self):

        super().__init__(user_solution, suggested_solution, solution_filename, success_message)
        self.num_random_test_cases = 100

        self.fixed_test_cases = [
            [],
            [],
            [],
            [],
            []
        ]
```

You must override the `test_case_to_string` method to format a test case for printing by returning a single string. In the example below, the test case is unpacked into two variables (`a` and `b`), and their values are inserted into f-strings. A new line is inserted between the two arguments to print each on a separate line.

```python
    def test_case_to_string(self, test_case) -> str:
        a, b = test_case
        return f'a = {a}' + '\n' + f'b = {b}'
```

You have plenty of flexibility in how you format a test case for output. Just keep in mind that the main goal is to make the output easy to read and understand.

If your exercise includes random test cases, override the `generate_random_test_case` method. In the example below, the method returns a list of two arguments, each a random number between -100 and 100.

Remember: every test case must be a list of arguments, even if a test case only contains a single argument.

```python
    def generate_random_test_case(self) -> list:
        return [random.randint(-100, 100), random.randint(-100, 100)]
```

Finally, replace `ExerciseName` below with the name of your new exercise class.

```python
if __name__ == "__main__":
    exercise = ExerciseName()
    exercise.run()
```

<BR>

************

[![Skillz Catalog](../graphics/PySkillzFooter.png)](skillz-catalog)
