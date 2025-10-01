# Creating a Custom Playground

You don’t have to contribute directly to the main PySkillz repository to take advantage of its architecture. You can also **create your own standalone playground**, which is perfect if you’re a teacher building custom worksheets for your students, or if you want to focus on a specific topic in isolation. Setting this up is straightforward and only requires a few steps.

# Create a New Python Project on Tech.io

Start on the [Tech.io](https://tech.io) front page and click **“Create a playground.”** On the next screen, choose **“Python Project.”**

Tech.io will generate a few default files you won’t need, and you’ll also need to copy some files from the PySkillz repository to get the proper structure in place. The goal is to replicate the following folder layout in your GitHub repository:

```
📁 graphics

📂 markdowns

📂 python-project
    📂 ____new_exercises____
        📂 ____exercise_template____
            📄 exercise_name.md
            📄 exercise_name.py
            📄 exercise_name_solution.py
            📄 exercise_name_test.py
        📄 template_generator.py
    📂 ____tools____
        📄 pyskillz_tools.py

📄 .gitignore

📄 techio.yml
```

Once this structure is set up, you can use **the same techniques described throughout this guide** to build and organize your own exercises, then link to them from your Markdown pages.

---

# Owning Your Playground

When you create your own playground, you are the **owner** of both the Tech.io playground and the corresponding GitHub repository. This means the instructions in the [Submit Your Exercise](submit-your-exercise) section no longer apply.

Instead, updating your playground is as simple as committing and pushing your changes to your repository:

```bash
git add .
git commit -a -m "Description of changes"
git push origin master
```

Because your playground is independent, **version control for `pyskillz_tools.py` is entirely manual**. To keep your playground up to date, check the main PySkillz repository periodically and pull in any changes made to `pyskillz_tools.py`.

---

# You're in Control

Creating your own playground gives you full creative freedom. You can structure lessons the way you want, experiment with custom exercise types, and deploy new content whenever you’re ready — all while leveraging the power of the PySkillz architecture.

Good luck, and have fun building!

<BR>

************

[![PySkillz](../../graphics/PySkillzFooter.png)](skillz-catalog)
