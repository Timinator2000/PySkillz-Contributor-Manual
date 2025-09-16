# Creating a New Exercise with the Template Generator

Creating a new exercise from scratch is quick and easy thanks to the **exercise template generator** included in the `python-project` folder. Instead of writing everything manually, you only need to provide the function definition that will be shown to the learner. From that, the generator automatically produces all the files needed for your exercise, with much of the boilerplate already filled in.

To help you understand how this works, we’ll first look at a **Tech.io web-based version** of the generator. This version is for experimentation only—it lets you try out the process without creating files on your computer.

A few important notes when experimenting:

* You **must change the exercise name**. The placeholder `exercise_name` is reserved for demonstration.

* Every parameter in your function must have a **type hint**, and the function itself must have a **return type hint** as well.

* If your function’s return type is `None`, the generator will produce a `PrintBasedExercise`. Any other return type results in a standard `Exercise`.

* Nothing generated in Tech.io is written to your local project. While you *could* copy and paste the code, this tool is meant only for getting familiar with how an exercise is structured and which files are created.

When you run the generator, you’ll see **four files created automatically**. These are the building blocks of every exercise.

> ⚠️ **Gotcha:** Tech.io code blocks must be syntactically correct. Make sure to include `pass` as the only line inside your function so the code runs without errors.

<BR>

> 📖 **Coming up next:** On the next page, we’ll break down each of the four generated files and explain their purpose.

<BR>

@[Enter a Function Signature for a New Exercise]({"stubs": ["tools/template_generator_techio/template_generator_techio.py"], "command": "python3 tools/template_generator_techio/template_generator_techio_test.py"})

