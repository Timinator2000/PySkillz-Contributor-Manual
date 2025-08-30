# Step 3: Start a New Exercise with the Template

Creating a new exercise from scratch is quick and easy thanks to the exercise template provided in the python-project folder. This template gives you a ready-made shell that includes all the required files.

```text
📂 python-project
    📂 ----new_exercises----
        📂 ----exercise_template----
            🗋 exercise_name.md
            🗋 exercise_name.py
            🗋 exercise_name_solution.py
            🗋 exercise_name_test.py
```

To create your own exercise:

1. Make a __full copy__ of the ----exercise_template---- folder inside the ----new_exercises---- folder.

2. Rename the copied folder and all of its files to match the name of your new exercise.

    * ✅ Use __underscores instead of spaces__ in file and folder names.

    * ✅ Keep file endings (`_solution.py`, `_test.py`) intact.

Your structure should now look something like this:

```
📂 python-project
    📂 ----new_exercises----
        📂 ----exercise_template----
            🗋 exercise_name.md
            🗋 exercise_name.py
            🗋 exercise_name_solution.py
            🗋 exercise_name_test.py
        📂 my_new_exercise
            🗋 my_new_exercise.md
            🗋 my_new_exercise.py
            🗋 my_new_exercise_solution.py
            🗋 my_new_exercise_test.py
```

With the folder and filenames in place, your exercise shell is ready. Now it’s time to start filling in the files to bring your exercise to life.

# Step 4




# THIS CAN PROBABLY ALL GO AWAY

To create a new exercise, three files must be placed together in the folder you created above:

* `exercise_name.py`
  * The code block presented to the end-user to solve.

* `exercise_name_solution.py`
  * Your working solution to the exercise.
    * The grader uses this file to determine the expected output.
    * After the end-user successfully completes the exercise, this entire file is displayed as the suggested solution.
  
* `exercise_name_test.py`
  * The exercise subclass that defines the specifics of this exercise, including:
    *  Static test cases for validation.
    *  The algorithm used to generate random test cases.
    *  A success message display after the end-user completes the exercise.

<BR>

These three files must be placed inside a folder named after the exercise itself. __Naming conventions are critical__ — the exercise architecture relies on these conventions to correctly locate the files it needs in order to execute successfully.

        📂 exercise_name<BR>
            🗋 exercise_name.py<BR>
            🗋 exercise_name_solution.py<BR>
            🗋 exercise_name_test.py<BR>

<BR>

Consider the “Hello, World!” example. Following the steps above, the folder and file structure looks like this:

        📂 hello_world<BR>
            🗋 hello_world.py<BR>
            🗋 hello_world_solution.py<BR>
            🗋 hello_world_test.py<BR>
<BR>

Finally, the `exercise_name` folder must be placed inside an __exercise group__ folder. A exercise group is a collection of exercises that are displayed together on a single markdown page.

For example, consider the [PySkillz Welcome](welcome) page. This page introduces the two types of exercises — print-based exercises and exercises that return an answer. Both of these exercises are grouped into an exercise group called `welcome`.

The resulting structure looks like this:

📂 python-project<BR>
    📂 welcome<BR>
        📂 hello_world<BR>
            🗋 hello_world.py<BR>
            🗋 hello_world_solution.py<BR>
            🗋 hello_world_test.py<BR>
        📂 add_two_numbers<BR>
            🗋 add_two_numbers.py<BR>
            🗋 add_two_numbers_solution.py<BR>
            🗋 add_two_numbers_test.py<BR>

On the next page, we'll explore the details of each of the three Python files that make up an exercise.

<BR>

************

[![Skillz Catalog](../graphics/PySkillzFooter.png)](skillz-catalog)
