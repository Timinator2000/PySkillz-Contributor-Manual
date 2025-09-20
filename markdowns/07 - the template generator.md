# The Template Generator

Let’s start by looking at a few folders and files inside the `python-project` folder:

```text
📂 python-project
    📂 ____new_exercises____
        📂 ____exercise_template____
            📄 exercise_name.md
            📄 exercise_name.py
            📄 exercise_name_solution.py
            📄 exercise_name_test.py
        📄 README.md
        📄 template_generator.py
````

To use the template generator, follow these steps:

1. Find the following line in `template_generator.py`:

   ```python
   function_signature = "def exercise_name(param1: str, param2: int) -> None:"
   ```

2. Change the function signature to match your new exercise. For example:

   ```python
   function_signature = "def my_cool_exercise(some_string: str, some_integer: int) -> None:"
   ```

3. Run the script. Your new exercise will appear inside `____new_exercises____`:

   ```text
   📂 ____new_exercises____
       📂 my_cool_exercise
           📄 my_cool_exercise.md
           📄 my_cool_exercise.py
           📄 my_cool_exercise_solution.py
           📄 my_cool_exercise_test.py
   ```

That’s all there is to it! 🎉 If you’d rather build your files directly from the template, read on.

# Creating a New Exercise By Hand

Why might you do this? Sometimes you want more control or just prefer the learning experience.

1. Make a **full copy** of the `____exercise_template____` folder inside `____new_exercises____`.

2. Rename the copied folder and all of its files to match the name of your new exercise.

   * ✅ Use **underscores instead of spaces** in file and folder names.

   * ✅ Keep file endings (`_solution.py`, `_test.py`) intact.

# Final Result

Your project folder should now look like this:

```text
📂 python-project
    📂 ____new_exercises____
        📂 ____exercise_template____
            📄 exercise_name.md
            📄 exercise_name.py
            📄 exercise_name_solution.py
            📄 exercise_name_test.py
        📂 my_cool_exercise
            📄 my_cool_exercise.md
            📄 my_cool_exercise.py
            📄 my_cool_exercise_solution.py
            📄 my_cool_exercise_test.py
        📄 README.md
        📄 template_generator.py
```

At this point, your folder structure is complete and your exercise shell is ready. 🎯

If you used the template generator, a lot of the setup has been done for you — but there are still a few things you must add yourself:

✍️ **Write the solution** in the `_solution.py` file.

✅ Define the `success_message`.

🧪 Add a few `fixed_test_cases`.

🎲 (Optional) Implement random test case generation if your exercise needs it.

Once those pieces are in place, you’re ready to test your new exercise! 🚀

<BR>

************

[![Skillz Catalog](../graphics/PySkillzFooter.png)](skillz-catalog)
