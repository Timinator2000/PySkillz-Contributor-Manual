# Step 6: Submit Your Exercise to GitHub

Once your new exercise is complete and tested locally, the final step is to __push your changes to your fork on GitHub__ and open a __pull request__ to the main PySkillz repository.

## Add and commit your changes

From the root of your local fork, use Git to stage and commit your new exercise:

```bash
git add python-project/----new_exercises----/my_new_exercise
git commit -m "Add new exercise: my_new_exercise"
```

## Push to your fork

```bash
git push origin master
```

_(Replace `master` with your branch name if you are using a feature branch.)_

## Open a Pull Request (PR)

1. Go to your fork on GitHub.

1. Click __Compare & pull request__.

1. Make sure the __base repository__ is the main PySkillz repository and the base branch is master.

Give your PR a clear title, e.g., "Add new exercise: my_new_exercise".

In the description, include:

Skill topic and skill group for placement.

Any notes about random test cases or special instructions for reviewers.

Submit the pull request.

4. Review and Merge

The PySkillz team will review your PR, provide feedback if needed, and merge it into the main repository.

Once merged, your exercise becomes live in the playground for learners!

💡 Tip: Always double-check your folder and file names before committing. GitHub is case-sensitive, and the playground relies on the exact naming conventions.