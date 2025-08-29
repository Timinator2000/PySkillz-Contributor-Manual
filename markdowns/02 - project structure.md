# Step 2: Explore the Project Structure

Now that you’ve cloned the repository, let’s take a tour of the main folders and files you’ll be working with:

📁 graphics

This folder contains images and other media used in exercises or documentation.

📂 markdowns

* This is where the written instructions for exercises live.

* Organized by __skill topic__ (e.g., loops, functions, data structures).

* Each topic contains one or more __exercise group__ markdown files (.md) that hold the descriptions, prompts, and explanations.

📂 python-project

This is where the actual Python code for each exercise lives.

* Organized first by __exercise group__.

* Inside each group, each __exercise__ has its own folder.

* A typical exercise folder includes:

  * `exercise_name.py` → The starter file learners will work on.

  * `exercise_name_solution.py` → The contributor solution, used to generate expected results for the exercise.

  * `exercise_name_test.py` → The __exercise subclass__ that defines test cases, a success message and a few other exercise components.

🗋 .gitignore

Specifies which files/folders Git should ignore (temporary files, caches, etc.).

🗋 techio.yml ⚠️

Configuration file used by the Tech.io platform to control the layout of the PySkillz playground.

* __Contributors should never modify this file.__

* Only PySkillz team members are allowed to update it, because any change directly affects how the playground is displayed to learners.

👉 As a contributors, you will spend the vast majority of your time in the `python-project` folder where you add the starter code, solution, and tests for your new exercise.

# .gitignore

The `.gitignore` file tells Git which files or folders it should __ignore__ when tracking changes. This helps keep the repository clean and prevents unnecessary or temporary files from being committed.

Currently, the PySkillz __.gitignore__ contains:

```text
**/__pycache__/
```

__What this does__

* Python automatically creates `__pycache__` folders to store compiled bytecode (`.pyc` files).

* These files are __generated automatically by Python__ not by your editor or IDE.

* Ignoring them keeps commits cleaner and avoids potential conflicts between different systems or Python versions.

__Other files contributors might want to ignore__

Depending on the tools you use, you might also see or want to add:

| Tool / OS	| Files/Folders to Ignore |
|:-----|:-----|
| VSCode | `.vscode/` |
| PyCharm | `.idea/` |
| OS-specific | macOS `.DS_Store`, Windows `Thumbs.db` |
| Python packaging | `*.egg-info/`, `dist/`, `build/` |
| Temp files | `*.tmp`, `*.log` |

>⚠️ __Important__: Contributors should __never modify the repository’s__ `.gitignore`. If you want to ignore personal editor or OS files, use a local or global Git ignore instead. This keeps the main repository clean and prevents accidental overwrites.

# Conceptual Project Snapshot

In the repository, you’ll see many more files, and the file names will reflect the actual exercise names. Conceptually, however, the project structure looks like this:

```
📁 graphics

📂 markdowns<BR>
    📂 skill topic
        🗋 exercise group.md
        🗋 exercise group 2.md
    📂 skill topic 2
        🗋 exercise group 3.md<BR>
        🗋 exercise group 4.md<BR>

📂 python-project<BR>
&nbsp;&nbsp;&nbsp;&nbsp;📂 exercise group<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📂 exercise_name<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 exercise_name.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 exercise_name_solution.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 exercise_name_test.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📂 exercise_name_2<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 exercise_name_2.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 exercise_name_2_solution.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 exercise_name_2_test.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📂 exercise_name_3<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 exercise_name_3.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 exercise_name_3_solution.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 exercise_name_3_test.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;📂 exercise group 2<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📂 exercise_name_4<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 exercise_name_4.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 exercise_name_solution_4.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 exercise_name_test_4.py<BR>

🗋 .gitignore

🗋 techio.yml
```

<BR>

************

[![Skillz Catalog](../graphics/PySkillzFooter.png)](skillz-catalog)
