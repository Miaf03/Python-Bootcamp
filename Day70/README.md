
# 🧠 Git & GitHub Cheat Sheet

## Basic Setup

```bash
# Configure user info
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"

# Check configuration
git config --list
```


## Starting or Cloning a Repository

```bash
# Initialize a new repository
git init

# Clone an existing repository
git clone <repository-url>
```


## Working with Changes

```bash
# Check status
git status

# Add files to staging
git add <file>

# Add all files
git add .

# Commit changes with a message
git commit -m "Commit message"

# Commit changes and skip staging (except new files)
git commit -am "Commit message"

# View commit history
git log
```


## Branching & Merging

```bash
# Create a new branch
git branch <branch-name>

# Switch branch
git checkout <branch-name>

# Create and switch in one command
git checkout -b <branch-name>

# Merge a branch into current
git merge <branch-name>

# Abort merge
git merge --abort

# Delete branch
git branch -d <branch-name>

# Delete branch forcefully
git branch -D <branch-name>

# List merged branches
git branch --merged

# List unmerged branches
git branch --no-merged
```


## Tags & Versioning

```bash
# List tags
git tag

# Create tag
git tag -a "v1.0.0" <hash> -m "Message"

# Show tag info
git show v1.0.0

# Push tags
git push origin --tags

# Delete local tag
git tag -d v1.0.0

# Delete remote tag
git push origin :refs/tags/v1.0.0
```


## Working with GitHub

```bash
# Connect local repo to GitHub
git remote add origin <repository-url>

# View remote repos
git remote -v

# Rename remote
git remote rename <old> <new>

# Remove remote
git remote remove <name>

# Push changes
git push -u origin main

# Force push
git push --force

# Pull latest changes
git pull origin main
```


## Undo & Fix Mistakes

```bash
# Unstage file (remove from staging)
git reset <file>

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (staging + working directory)
git reset --hard HEAD~1

# Undo changes in a file
git checkout -- <file>
```


## Logs & History

```bash
# Short commit history
git log --oneline

# Detailed logs
git log -p
git log --stat

# Search commits by author
git log --author="Name"

# Graph history
git log --oneline --graph --all
```


## SSH Keys

```bash
# Generate SSH key
ssh-keygen -t rsa -b 4096 -C "youremail@example.com"

# Add key to system
ssh-add ~/.ssh/your_key

# Test connection
ssh -T git@github.com
```

```bash
# Mac specific: add to Keychain
ssh-add -K ~/.ssh/your_key
eval "$(ssh-agent -s)"
```


## Git Stash

```bash
# Save changes temporarily
git stash

# Save with message
git stash save "message"

# List stashes
git stash list

# Apply stash
git stash apply stash@{n}

# Apply and remove stash
git stash pop stash@{n}

# Create branch from stash
git stash branch branch_name
```


## Useful Shortcuts

```bash
# Compare changes before commit
git diff

# See branches
git branch

# See short commit history
git log --oneline
```