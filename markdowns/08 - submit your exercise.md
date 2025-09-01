# Step 7: Submit Your Exercise to GitHub

Once your new exercise is complete and tested locally, the final step is to __push your changes to your fork on GitHub__ and open a __pull request__ to the main PySkillz repository.

## Check if your fork is up-to-date

* On GitHub: Look for a message indicating your branch is behind the main repository.

* Locally:

```bash
git fetch upstream
git log --oneline master..upstream/master
```

* If this shows commits, then your fork is behind.

* If it shows nothing, you’re already up-to-date.


## Sync your fork (if needed)

* Add the main PySkillz repo as an upstream remote (if not already added):

```bash
git remote add upstream https://github.com/Timinator2000/PySkillz.git
```

* Fetch the latest changes from upstream:

```bash
git fetch upstream
```

* Merge changes into your local `master` branch:

```bash
git checkout master
git merge upstream/master
```

* Resolve any merge conflicts if prompted.

* Push your updated `master` branch to your fork:

```bash
git push origin master
```

>💡Tip: Always sync your fork before starting a new exercise to minimize conflicts.

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

1. Make sure the __base repository__ is the main PySkillz repository and the base branch is `master`.

1. Give your PR a clear title, e.g., `"Add new exercise: my_new_exercise"`.

1. In the description, include:

    * Skill topic and skill group for placement.

     * Any notes about random test cases or special instructions for reviewers.

1. Submit the pull request.

## Review and Merge

* The PySkillz team will review your PR, provide feedback if needed, and merge it into the main repository.

* Once merged, 🎉 your exercise becomes live in the playground for learners!

>💡 Tip: Always double-check your folder and file names before committing. GitHub is case-sensitive, and the playground relies on the exact naming conventions.