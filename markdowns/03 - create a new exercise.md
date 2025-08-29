# Placing Your Exercise



# Creating Your Exercise

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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📂 exercise_name<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 exercise_name.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 exercise_name_solution.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 exercise_name_test.py<BR>

<BR>

Consider the “Hello, World!” example. Following the steps above, the folder and file structure looks like this:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📂 hello_world<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 hello_world.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 hello_world_solution.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 hello_world_test.py<BR>
<BR>

Finally, the `exercise_name` folder must be placed inside an __exercise group__ folder. A exercise group is a collection of exercises that are displayed together on a single markdown page.

For example, consider the [PySkillz Welcome](welcome) page. This page introduces the two types of exercises — print-based exercises and exercises that return an answer. Both of these exercises are grouped into an exercise group called `welcome`.

The resulting structure looks like this:

📂 python-project<BR>
&nbsp;&nbsp;&nbsp;&nbsp;📂 welcome<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📂 hello_world<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 hello_world.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 hello_world_solution.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 hello_world_test.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📂 add_two_numbers<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 add_two_numbers.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 add_two_numbers_solution.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 add_two_numbers_test.py<BR>

On the next page, we'll explore the details of each of the three Python files that make up an exercise.

<BR>

************

[![Skillz Catalog](../../graphics/PySkillzFooter.png)](skillz-catalog)
