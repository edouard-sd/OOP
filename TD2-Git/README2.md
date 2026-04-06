# TD2: My Little Guide to Git & GitHub

Here is the summary of the commands I used during this TD to manage the versions of my project.

---

## Inspecting my repository

- **Check the status:** `git status`
  - *Shows me what I haven't committed or pushed yet.*
- **My full history:** `git log`
- **My quick history:** `git log --oneline`
- **What I modified:** `git diff`
  - *Handy to see my changes since the last commit.*

## Saving my work

- **Add (staging):** `git add .` (or `git add readme.txt` for one file)
- **Validate (commit):** `git commit -m "Add readme file"`

## My Branches

- **See all my branches:** `git branch -a`
- **Create a branch:** `git branch feature-script`
- **Go to the branch:** `git checkout feature-script`
- **Create and go directly:** `git checkout -b dev`
- **See where I am:** `git branch` (there's a `*` next to it)

> **Note:** If I don't see one of my files (ex: `install.sh`), it's probably because I'm on the wrong branch.

## Merging & Cleaning my branches

1. I go back to main: `git checkout main`
2. I merge: `git merge feature-script`
3. I check that everything is there: `ls`
4. I delete the finished branch: `git branch -d feature-script`

## GitHub & Pushing my work

- **Link my folder to GitHub:**
  ```bash
  git remote add origin https://github.com/edouard-sd/OOP
  ```
- **Push to the server:**
  ```bash
  git push -u origin main
  ```
- **Tada!** All my code is now visible on GitHub, ready to be graded!
