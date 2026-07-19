</Markdown>

# Day 29 Notes
 - git workflows

# Concepts Learned
 - inspect repository for unstaged files, staged files, and the state of the reposity
 - know exactly what has been added/deleted, changed, inserted, modified
 - interactively decide whether to stage certain modifications, cancel, ignore, or postpone (git add -p)

# Key Commands
 - git status
 - git add -p, git add, git commit -m "message", git push, git branch, git log --oneline, git diff
 - git fetch, git restore <file>, git restore . (restores everything that are unstaged)
 - git restore --staged <filename>, after file has been staged via git add <file>, it will be unstaged and restored to previous committed version
 - git restore . (restores all unstaged modifications in the repository to its previous committed state)
 - git revert <commit-hash> -- restores all files that have been changed into that commit-hash's version
 - git restore --source=<commit-hash> <filePath>, restores local copy to a certain version of the file in the current repo for modification.  (in situations where you realized that that version of the file is the perfect version) 

# Key Observations
Commit early and often: 
  - Even if your code is messy or broken, creating a local "WIP" (Work In Progress) commit 
    gives you a snapshot you can always return to.
- Avoid git reset --hard unless you are certain: 
  Running git reset --hard is one of the few destructive commands in Git because it wipes 
  away both staged and unstaged changes simultaneously. 
- Stick to git restore for targeted safety.
- Your Safety Net (git reflog): If you ever feel like you completely destroyed your repository or lost a commit during a 
  complex rebase/reset, run git reflog. Git keeps a hidden log of every single movement of the $HEAD$ pointer, allowing 
  you to recover almost anything you've touched in the last 90 days.

# Lessons Learned
- use git diff <file> to check state of local file vs repository
  you will be able to see exactly what were changed, like inserted lines, deleted lines, moved lines, modified lines
  you will also be able to see whether those changes are accidental, intentional, prototype, or ready for commit
- git diff --word-dif: ensure no accidental typos were introduced
- git diff <commit-hash1> <commit-hash2>
- Compare current code to a specific past commit	git diff <commit-hash>
- Compare literal tips of two branches	git diff branch1..branch2
- See only feature branch changes (PR Style)	git diff main...feature-branch
- Compare two specific historical commits	git diff hash1..hash2
- List changed files only (no code text)	git diff --name-only branch1..branch2

# Questions For Future Study
 - is there a way to automate the engineering workflow for git commit ? I guess the obvious answer is NO .. because 
   it needs inspection and a good engineering judgment to determine what gets committed and what doesn't.

