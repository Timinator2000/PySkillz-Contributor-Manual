![PySkillz](../graphics/PySkillzBanner.png)



Got it! You want to **clone a GitHub repository** to your local machine. Here’s a clear step-by-step:

---

### 1. Get the repository URL

* Go to the repository page on GitHub.
* Click the **Code** button (green).
* Copy the URL under **HTTPS** (e.g., `https://github.com/username/repo.git`) or **SSH** (if you set up SSH keys).

---

### 2. Open your terminal (Git Bash on Windows)

---

### 3. Choose a local folder

Navigate to the directory where you want the repo to live:

```bash
cd path/to/your/folder
```

---

### 4. Clone the repository

Run:

```bash
git clone https://github.com/username/repo.git
```

Replace the URL with your repository’s URL. This will create a folder with the repository’s content.

---

### 5. Go into the repository folder

```bash
cd repo
```

You now have the repo locally and can start working with it.

---

Optional: Check the remote:

```bash
git remote -v
```

This shows that `origin` points to GitHub.

---









Here you go — the **entire contributor manual** in one clean Markdown file. You can drop this straight into your repo as `CONTRIBUTING.md` or `docs/contributor-manual.md`.

---

````markdown
# PySkillz Contributor Manual

## 1. Getting Started  

### 1.1 Clone the repository  
```bash
git clone https://github.com/Timinator2000/PySkillz.git
cd PySkillz
````

---

### 1.2 Set up your environment

1. **Install Python 3.10+**

   * Check your version:

     ```bash
     python --version
     ```

     or

     ```bash
     python3 --version
     ```

2. **Create a virtual environment** (recommended)

   * On Linux/macOS:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   * On Windows (PowerShell):

     ```powershell
     python -m venv venv
     .\venv\Scripts\activate
     ```

   > After this, your terminal prompt should show `(venv)` — meaning you’re inside the isolated environment.

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **(Optional) Deactivate the environment**

   ```bash
   deactivate
   ```

---

### 1.3 Verify your setup

1. **Run the test suite**

   ```bash
   pytest
   ```

   * If all tests pass, your environment is set up correctly.

2. **Run a sample script**

   ```bash
   python examples/hello.py
   ```

   Expected output:

   ```
   ✅ Hello, PySkillz contributor! Your environment is ready to go.
   ```

✅ At this point your environment is ready for development.

---

## 2. Making Changes

* Keep commits **focused and small**.
* Write clear commit messages:

  ```bash
  git commit -m "Add exercise generator for while loops"
  ```
* Use `git status` and `git diff` often to review what you’re committing.
* Run tests with `pytest` before pushing changes.

---

## 3. Pushing to GitHub

1. Create a branch for your work:

   ```bash
   git checkout -b feature/my-new-feature
   ```

2. Push it to GitHub:

   ```bash
   git push origin feature/my-new-feature
   ```

3. Open a Pull Request (PR) from your branch into `master`.

---

## 4. Handling Pull Requests

### For Contributors

* Keep PRs focused on one change.
* Ensure your branch is up to date with `master`:

  ```bash
  git fetch origin
  git merge origin/master
  ```

### For Maintainers

You can handle PRs in **two ways**:

#### Option A: Merge on GitHub

* Review the PR in GitHub’s web interface.
* If approved, click **Merge pull request**.
* This merges all changes into `master`.

#### Option B: Merge Locally

1. Fetch the PR branch:

   ```bash
   git fetch origin pull/ID/head:temp-branch
   ```
2. Review/test it locally.
3. Merge into master:

   ```bash
   git checkout master
   git merge temp-branch
   ```
4. Push the updated master:

   ```bash
   git push origin master
   ```

---

## 5. Git Best Practices

* **Sync often**:

  ```bash
  git fetch origin
  git pull
  ```
* **Keep history clean**: squash trivial commits before pushing.
* **Never commit secrets or local config files.**
* **Use `.gitignore`** for editor settings, virtual environments, and build artifacts.

---

## 6. Communication

* Use GitHub Issues for bugs and feature requests.
* Discuss large changes before starting work.
* Be clear and concise in commit messages and PR descriptions.

---

```

---

Would you like me to also add a **"Repository Structure" section** at the top (showing where `examples/hello.py`, `requirements.txt`, and main code live), so new contributors immediately understand the layout?
```

