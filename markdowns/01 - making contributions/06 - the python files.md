# The Python Files

Every exercise requires three Python files:

* `exercise_name.py`
  * The __starter code__ presented to the learner.

* `exercise_name_solution.py`
  * Your __working solution__ to the exercise.
    * The grader uses this file to determine the expected output.
    * After the learner successfully completes the exercise, this entire file is displayed as the suggested solution.
  
* `exercise_name_test.py`
  * The __exercise subclass__ that defines the specifics of this exercise, including:
    *  Static test cases for validation.
    *  The algorithm used to generate any random test cases.
    *  A success message displayed after the learner completes the exercise.

The template generator uses the files in the `____exercise_template____` folder to build a starting template for you.

* If your function’s return type is `None`, the generator creates a `PrintBasedExercise` template.
* If your function returns anything else, the generator creates an `Exercise` template.

Now, let’s take a closer look at each file so you know **exactly what to edit** to get your new exercise up and running.

*****************

<BR>

>The following discussion explains the manual process of creating an exercise **without** the generator. When you use the generator, some **(but not all)** of these steps will already be handled for you, but it’s still useful to understand how everything fits together.

# exercise_name.py

The contents of this file are shown to the user in the code window. Keep it very short.

For exercises that have input parameters and return values (`pyskillz_tools.Exercise`), provide only a minimal function stub.

```python
def exercise_name(a: int, b: int) -> int:
    return # Your code goes here.
```

For exercises that take input and require the user to print an answer (`pyskillz_tools.PrintBasedExercise`), include a few extra comment lines. Since all `print` output is graded, remind users they can use `sys.stderr` for debug messages.

```python
def exercise_name(a: int, b: int) -> None:
    # Your code goes here.
    
    # Write an answer using print
    # To debug: import sys at the top of this script
    #           print('Debug messages...', file=sys.stderr, flush=True)
```

# exercise_name_solution.py

This file contains the suggested solution along with any alternate soltuions. The primary solution is used by the grader to check correctness. Once the user completes the exercise successfully, the full contents of this file are displayed.

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

The first section is reserved for setup and __must not be modified__. It imports the exercise framework from `pyskillz_tools.py`.

```python
###############################################################################################################
# Environment Setup - Do not change anything in this section.
###############################################################################################################

import os
import sys
import random

# Normalize path for current OS. Split the path into directory and filename.
dir_path, _ = os.path.split(os.path.normpath(__file__))

# Add tools directory to the OS PATH
sys.path.insert(0, os.path.join(dir_path, '..', '..', '____tools____'))

try:
    import pyskillz_tools

except ImportError:
    print(f'Import Error: pyskillz_tools.py needs to be in the ____tools____ folder, one level deep from python-project.')

###############################################################################################################
# End Setup
###############################################################################################################
```

Next, define the message shown to the user when the exercise is completed successfully. Place this definition outside the class for easier formatting. A multiline string can be used to include elements like bullet points or even a short Q&A (e.g., a joke).

For paragraphs that require automatic word wrapping, break the text into separate lines and concatenate them. This keeps the text easy to read in the code while still displaying correctly to the user.

```python
success_message = '''


'''

success_message += ''
success_message += ''
success_message += ''
```

Next, declare your exercise class by choosing one of the following lines. Each option specifies the exercise type your class will inherit from. Be sure to replace `ExerciseName` with the actual name of your exercise, matching the `exercise_name` wording used for your files.

```python
class ExerciseName(pyskillz_tools.Exercise):
class ExerciseName(pyskillz_tools.PrintBasedExercise):
```

The first line of the class constructor (`__init__` ) must remain unchanged. It calls the superclass constructor, passing the full filename and the success message.

On the second line, specify the parameter names. The superclass uses these names when displaying a test case to the learner. 

On the third line, specify the number of random test cases your exercise should generate. Random test cases are not required but are highly encouraged — they are simple to create and add robustness to the testing strategy.

Finally, define a list of `fixed_test_cases`. Each test case is itself a list of arguments. The stub code below includes 5 empty test cases as placeholders, but you may use more or fewer. Insert arguments into each test case placeholder.

Remember: every test case must be a list of arguments, even if there is only one. For example:

* A single integer argument → `[5]`

* A list of integers as the lone argument → `[[1, 2, 3]]`

```python
    def __init__(self):

        super().__init__(__file__, success_message)
        self.parameter_names = ['param_1', 'param_2']
        self.num_random_test_cases = 1000

        self.fixed_test_cases = [
            [],
            [],
            [],
            [],
            []
        ]
```

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

On the next page, we'll run the generator and create some real files. You'll see the generator does many of the steps above for you, but it cannot do them all!

************

[![PySkillz](../../graphics/PySkillzFooter.png)](skillz-catalog)
